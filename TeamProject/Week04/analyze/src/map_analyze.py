from flask import Flask, render_template, request, jsonify, send_from_directory
import pymysql
import os
import math

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(base_dir, "img")

# DB 설정
db_config = {
	'host': 'localhost',
	'user': 'root',
	'password': '123456',
	'db': 'pohang_analyze',
	'charset': 'utf8',
	'cursorclass': pymysql.cursors.DictCursor  # 결과를 딕셔너리 형태로 받기 위함
}


def get_gstats():
	"""DB에 저장된 통계값이 있으면 가져오고, 없으면 계산합니다."""
	conn = pymysql.connect(**db_config)
	cursor = conn.cursor()

	try:
		cursor.execute("SELECT min_co, max_co FROM floating_stats LIMIT 1")
		row = cursor.fetchone()

		if row: # 있으면 가져옴
			return row['min_co'], row['max_co']
		else: # 없으면 안해도되는데 계산
			cursor.execute("SELECT COUNT(*) AS cnt FROM floating")
			total_cnt = cursor.fetchone()['cnt']

			if total_cnt > 0:
				offset_val = max(0, int(total_cnt * 0.95) - 1)

			cursor.execute("SELECT MIN(co) AS min_co FROM floating")
			g_min = cursor.fetchone()['min_co'] or 0

			cursor.execute("SELECT co AS max_co FROM floating ORDER BY co ASC LIMIT 1 OFFSET %d" % offset_val)
			res_max = cursor.fetchone()
			g_max = res_max['max_co'] if res_max else 10000

			# 계산 결과 저장
			cursor.execute("INSERT INTO floating_stats (min_co, max_co) VALUES (%s, %s)", (g_min, g_max))
			conn.commit()

			return (g_min, g_max)

	except Exception as e:
		print(f"통계 초기화 오류: {e}")
	finally:
		cursor.close()
		conn.close()


def calculate_metric_score(current_val, avg_val, avg_score, is_reverse=False):
	# 0점, 50점 (데이터x) avg_score점 (평균), 최대 100점
	if avg_val == 0:
		return 50.0

	if is_reverse:
		if current_val == 0: score = 100.0
		else: score = (avg_val / current_val) * avg_score
	else: score = (current_val / avg_val) * avg_score

	return min(100.0, score)

def generate_report(counts, db_config):
	conn = pymysql.connect(**db_config)
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	# metric_report 로드
	cursor.execute("SELECT * FROM metric_report")
	metrics = {row['category']: row for row in cursor.fetchall()}

	scores = {}
	reports = []
	total_score = 0.0
	metrics['hospital']['weight'] += metrics['bank']['weight']
	metrics['school']['weight'] += metrics['academy']['weight'] + metrics['library']['weight']

	scores['floating'] = calculate_metric_score(counts.get('floating', 0), metrics['floating']['avg_val'], metrics['floating']['avg_score'])
	scores['cafe'] = calculate_metric_score(counts.get('cafe', 0), metrics['cafe']['avg_val'], metrics['floating']['avg_score'], True)
	scores['cafe_distance'] = calculate_metric_score(counts.get('cafe_distance', 0), metrics['cafe_distance']['avg_val'], metrics['floating']['avg_score'])
	scores['busstop'] = calculate_metric_score(counts.get('busstop', 0), metrics['busstop']['avg_val'], metrics['floating']['avg_score'])
	scores['accom'] = calculate_metric_score(counts.get('accom', 0), metrics['accom']['avg_val'], metrics['floating']['avg_score'])

	scores['hospital'] = calculate_metric_score(counts.get('hospital', 0), metrics['hospital']['avg_val'], metrics['hospital']['avg_score'])
	scores['school'] = calculate_metric_score(counts.get('school', 0), metrics['school']['avg_val'], metrics['school']['avg_score'])

	for metric in scores.keys():
		total_score += scores[metric] * metrics[metric]['weight']

		# 90점 이상 리포트 추가
		if scores[metric] >= 90 and metrics[metric]['description']:
			reports.append(metrics[metric]['description'])

	cursor.close()
	conn.close()

	return {
		'total_score': round(total_score, 0),
		'item_scores': scores,
		'reports': reports
	}

@app.route('/img/<path:filename>')
def serve_image(filename):
	return send_from_directory(IMAGE_DIR, filename)


@app.route('/')
def index():
	return render_template('index.html')

def calculate_distance(lat1, lon1, lat2, lon2):
	dx = (lat2 - lat1) * 111000
	dy = (lon2 - lon1) * 88000
	return math.sqrt(dx ** 2 + dy ** 2)

# 공통 쿼리 함수 (반경 검색용)
def get_db_nearby(table_name, lat, lon, radius):
	# 위경도 델타값 계산 (반경을 도 단위로 변환)
	lat_deg = radius / 111000
	lon_deg = radius / 88000

	conn = pymysql.connect(**db_config)
	cursor = conn.cursor()

	# 사각형 범위로 1차 필터링 후 원형 거리 계산 (성능을 위해 BETWEEN 활용)
	sql = f"SELECT * FROM {table_name} WHERE (lat BETWEEN %s AND %s) AND (lon BETWEEN %s AND %s) AND ST_Distance_Sphere(point(lon, lat), point(%s, %s)) <= %s"
	cursor.execute(sql, (lat - lat_deg, lat + lat_deg, lon - lon_deg, lon + lon_deg, lon, lat, radius))
	nearby_points = cursor.fetchall()

	cursor.close()
	conn.close()
	return nearby_points

@app.route('/api/analyze')
def analyze():
	lat = float(request.args.get('lat'))
	lon = float(request.args.get('lon'))
	radius = float(request.args.get('radius', 500))

	# 각 테이블에서 근처 데이터 가져오기
	n_floating = get_db_nearby('floating', lat, lon, radius)
	n_cafe = get_db_nearby('cafe', lat, lon, radius)
	n_hospital = get_db_nearby('hospital', lat, lon, radius)
	n_busstop = get_db_nearby('busstop', lat, lon, radius)
	n_accom = get_db_nearby('accom', lat, lon, radius)
	n_bank = get_db_nearby('bank', lat, lon, radius)
	n_school = get_db_nearby('school', lat, lon, radius)
	n_academy = get_db_nearby('academy', lat, lon, radius)
	n_library = get_db_nearby('library', lat, lon, radius)

	# 가장 가까운 카페 거리 계산
	cafe_dist_val = radius
	min_cafe_dist = "반경 내 없음"
	if n_cafe:
		dists = [calculate_distance(lat, lon, p['lat'], p['lon']) for p in n_cafe]
		cafe_dist_val = min(dists)
		min_cafe_dist = "%.1fm" % cafe_dist_val

	# 행정동 최빈값 구하기
	if n_floating:
		dongs = [p['admin_dong'] for p in n_floating]
		mode_dong = max(set(dongs), key=dongs.count)
		avg_floating = int(sum(p['co'] for p in n_floating) / len(n_floating))
	else:
		mode_dong = "데이터 없음"
		avg_floating = 0



	cafe_dist_val = radius
	if n_cafe:
		dists = [calculate_distance(lat, lon, p['lat'], p['lon']) for p in n_cafe]
		cafe_dist_val = min(dists)
	counts = {
		'floating': avg_floating,
		'cafe': len(n_cafe),
		'cafe_distance': cafe_dist_val,
		'hospital': len(n_hospital),
		'busstop': len(n_busstop),
		'accom': len(n_accom),
		'bank': len(n_bank),
		'school': len(n_school),
		'academy': len(n_academy),
		'library': len(n_library)
	}
	g_stats = get_gstats()
	analysis_result = generate_report(counts, db_config)

	dong_description = ""
	if mode_dong != "데이터 없음":
		conn = pymysql.connect(**db_config)
		cursor = conn.cursor()
		try:
			cursor.execute("SELECT description FROM dong_report WHERE admin_dong = %s", (mode_dong,))
			res = cursor.fetchone()
			if res and res['description']:
				dong_description = res['description']
		finally:
			cursor.close()
			conn.close()

	return jsonify({
		'dong': mode_dong,
		'avg_floating': f"{avg_floating}명",
		'cafe_count': f"{len(n_cafe)}개",
		'hospital_count': f"{len(n_hospital)}개",
		'busstop_count': f"{len(n_busstop)}개",
		'accom_count': f"{len(n_accom)}개",
		'bank_count': f"{len(n_bank)}개",
		'school_count': f"{len(n_school)}개",
		'academy_count': f"{len(n_academy)}개",
		'library_count': f"{len(n_library)}개",
		'points_floating': n_floating,
		'points_cafe': n_cafe,
		'points_hospital': n_hospital,
		'points_busstop': n_busstop,
		'points_accom': n_accom,
		'points_bank': n_bank,
		'points_school': n_school,
		'points_academy': n_academy,
		'points_library': n_library,
		'min_cafe': min_cafe_dist,
		'min_co': g_stats[0],
		'max_co': g_stats[1],
		'total_score': analysis_result['total_score'],
		'item_scores': analysis_result['item_scores'],
		'reports': analysis_result['reports'],
		'dong_report': dong_description
	})


@app.route('/api/all_data')
def get_all_data():
	requested = request.args.get('types', '').split(',')
	conn = pymysql.connect(**db_config)
	cursor = conn.cursor()

	g_stats = get_gstats()

	data = {}

	# 유동인구 통계
	data['min_co'] = g_stats[0]
	data['max_co'] = g_stats[1]

	# 요청된 타입별 전체 데이터 가져오기
	for t in requested:
		if t:
			cursor.execute("SELECT * FROM %s" % t)
			data[t] = cursor.fetchall()

	cursor.close()
	conn.close()
	return jsonify(data)


if __name__ == '__main__':
	app.run(port=5000, debug=True)
