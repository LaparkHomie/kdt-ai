import pymysql
import pandas as pd
import os

# CSV 폴더 경로
DATA_DIR = "../data/"

# 테이블명과 CSV 파일명, lat, lon, name, co(유동인구), admin_dong(행정동) 컬럼 매핑
table_mappings = {
	'floating': {
		'file': '유동인구.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', 'co': 'co', 'ADMIN_DONG': 'admin_dong'},
		'create_sql': "CREATE TABLE floating (lat DOUBLE, lon DOUBLE, co INT, admin_dong VARCHAR(100))"
	},
	'cafe': {
		'file': '카페.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '상호명': 'name'},
		'create_sql': "CREATE TABLE cafe (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'hospital': {
		'file': '병원.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '종별코드명': 'name'},
		'create_sql': "CREATE TABLE hospital (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'busstop': {
		'file': '버스정류장.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '버스정류장': 'name'},
		'create_sql': "CREATE TABLE busstop (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'accom': {
		'file': '숙박.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '표준산업분류명': 'name'},
		'create_sql': "CREATE TABLE accom (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'bank': {
		'file': '은행.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', 'BANK_NM': 'name'},
		'create_sql': "CREATE TABLE bank (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'school': {
		'file': '학교.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '학교명': 'name'},
		'create_sql': "CREATE TABLE school (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'academy': {
		'file': '학원.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '상권업종소분류명': 'name'},
		'create_sql': "CREATE TABLE academy (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	},
	'library': {
		'file': '도서관.csv',
		'cols': {'lat': 'lat', 'lon': 'lon', '도서관명': 'name'},
		'create_sql': "CREATE TABLE library (lat DOUBLE, lon DOUBLE, name VARCHAR(100))"
	}
}

metric_mappings = {
	'floating': {
		'avg_val': 811.91, 'avg_score': 70, 'weight': 0.25,
		'description': '유동인구 비중: 높은 유동인구를 보유한 핵심 요충지입니다.'
	},
	'cafe': {
		'avg_val': 21.13, 'avg_score': 80, 'weight': 0.15,
		'description': '경쟁 카페 밀집도: 인근 카페 밀집도가 낮아 신규 진입 시 전략적 입지입니다.'
	},
	'cafe_distance': {
		'avg_val': 130.0, 'avg_score': 80, 'weight': 0.20,
		'description': '가장 가까운 카페 거리: 기존 카페들과의 거리가 충분히 확보된 전략적 입지입니다.'
	},
	'hospital': {
		'avg_val': 12.92, 'avg_score': 80, 'weight': 0.10 / 2,
		'description': '생활 편의 시설 (병원/은행): 목적성이 분명하고 대기시간이 발생하는 인프라입니다. 이를 대상으로 전략을 구축하는 것을 권장합니다.'
	},
	'busstop': {
		'avg_val': 10.89, 'avg_score': 80, 'weight': 0.10,
		'description': '교통 시설 (버스정류장): 출근길 매출이 높습니다. 이른 시간에 오픈하는 것이 좋으며, 테이크아웃 비중이 높습니다.'
	},
	'accom': {
		'avg_val': 6.84, 'avg_score': 80, 'weight': 0.10,
		'description': '숙박 시설: 주말 매출 비중이 높습니다. 지역 특색을 살린 시그니처 메뉴와 포토존 구축이 권장됩니다.'
	},
	'bank': {
		'avg_val': 1.05, 'avg_score': 80, 'weight': 0.10 / 2,
		'description': ''
	},
	'school': {
		'avg_val': 1.21, 'avg_score': 80, 'weight': 0.10 / 3,
		'description': '교육 시설 (학교/학원/도서관): 학생 및 학부모층의 목적형 방문이 활발한 지역입니다. 긴 체류시간과 낮은 회전율을 보완할 수 있는 사이드 메뉴 강화가 필요합니다.'
	},
	'academy': {
		'avg_val': 22.44, 'avg_score': 80, 'weight': 0.10 / 3,
		'description': ''
	},
	'library': {
		'avg_val': 0.15, 'avg_score': 80, 'weight': 0.10 / 3,
		'description': ''
	}
}

dong_feature = {
	'두호동': '#관광형 (숙박시설 밀집구역)',
	'대이동': '#에듀케어형 (학교/학원 밀집구역)',
	'오천읍': '#오피스밀집형 (병원 밀집구역)',
	'우창동': '#에듀케어형 (학교 밀집구역)',
	'장량동': '#오피스밀집형 (병원 밀집구역)',
	'중앙동': '#오피스밀집형 (병원/은행 밀집구역)'
}

def migrate():
	DATABASE_NAME = "pohang_analyze"
	# DB 연결 (처음엔 DB 없이 연결하여 CREATE DATABASE 수행)
	conn = pymysql.connect(host='localhost',
						   port=3306,
						   user='root',
						   password='123456',
						   charset='utf8')

	cursor = conn.cursor()

	try:
		# DB 생성 및 선택
		cursor.execute("CREATE DATABASE IF NOT EXISTS %s CHARACTER SET utf8;" % DATABASE_NAME)
		cursor.execute("USE %s;" % DATABASE_NAME)

		for table_name, info in table_mappings.items():
			print("[%s] 처리 중..." % table_name)

			# 기존 테이블 삭제 후 생성
			cursor.execute("DROP TABLE IF EXISTS %s" % table_name)
			cursor.execute(info['create_sql'])

			# CSV 읽기 (pandas를 사용하여 데이터 정제만 수행)
			file_path = os.path.join(DATA_DIR, info['file'])
			df = pd.read_csv(file_path)

			# 필요한 컬럼만 추출 및 이름 변경
			df_subset = df[list(info["cols"].keys())].copy()
			df_subset.rename(columns=info["cols"], inplace=True)

			# 결측치 제거
			df_subset = df_subset.dropna(subset=["lat", "lon"])

			# 데이터 삽입 SQL 구성
			sql = ("INSERT INTO %s (%s) VALUES (%s)"
				% (table_name, ", ".join(df_subset.columns), ", ".join(["%s"] * len(df_subset.columns))))
			cursor.executemany(sql, df_subset.values.tolist())

			# 성능을 위한 인덱스 생성
			cursor.execute("CREATE INDEX idx_%s_geo ON %s (lat, lon)" % (table_name, table_name))

		cursor.execute("DROP TABLE IF EXISTS floating_stats")
		cursor.execute("CREATE TABLE floating_stats(min_co INT, max_co INT);")

		# 행정동별 리포트
		sql = '''
		CREATE TABLE dong_report (
			admin_dong VARCHAR(100),		# 동명 
			description VARCHAR(300)		# 상권 설명
		)
		'''
		cursor.execute("DROP TABLE IF EXISTS dong_report")
		cursor.execute(sql)

		df_risk = pd.read_csv(DATA_DIR + "단기폐업 위험도.csv", encoding="utf-8")
		target_dongs = {'중앙동', '양학동', '우창동', '용흥동', '환여동', '두호동', '장량동', '상대동', '제철동', '효곡동', '대이동', '해도동', '죽도동', '송도동', '청림동', '기북면', '기계면', '장기면', '송라면', '호미곶면', '구룡포읍', '청하면', '흥해읍', '죽장면', '신광면', '오천읍', '연일읍', '대송면', '동해면' }
		dong_stats = df_risk.groupby('ADMIN_DONG')['단기폐업률(%)'].mean().to_dict()

		insert_data = []
		for dong in target_dongs:
			risk_text = ""
			if dong in dong_stats:
				if dong_stats[dong] >= 20:
					risk_text = "#폐업위험 (단기 폐업률 %.1f%%의 위험 지역)" % dong_stats[dong]
			feature_text = dong_feature.get(dong, "")

			insert_data.append((dong, (feature_text + " " + risk_text).strip()))
		cursor.executemany("INSERT INTO dong_report (admin_dong, description) VALUES (%s, %s)", insert_data)

		# 인프라별 리포트
		sql = '''
			CREATE TABLE metric_report (
			category			VARCHAR(100) PRIMARY KEY,
			avg_val				FLOAT,
			avg_score			INT,
			weight				FLOAT,
			description			VARCHAR(300)
		)
		'''
		cursor.execute("DROP TABLE IF EXISTS metric_report")
		cursor.execute(sql)

		for metric, info in metric_mappings.items():
			sql_insert = "INSERT INTO metric_report (category, avg_val, avg_score, weight, description) VALUES (%s, %s, %s, %s, %s)"
			cursor.execute(sql_insert, (metric, info['avg_val'], info['avg_score'], info['weight'], info['description']))

		conn.commit()
		print("\n모든 데이터가 성공적으로 MySQL로 이관되었습니다!")

	except Exception as e:
		print(f"\n오류 발생: {e}")
		conn.rollback()
	finally:
		cursor.close()
		conn.close()


if __name__ == "__main__":
	migrate()
