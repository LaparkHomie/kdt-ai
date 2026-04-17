import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import branca.colormap as cm

# 실행 방법: cmd에서 streamlit run pohang_information.py

# 1. 페이지 설정
st.set_page_config(page_title="포항 상권 입지 분석기", layout="wide")
st.title("포항시 실시간 입지 분석 (반경 250m)")

# --- [추가] 세션 상태 초기화 ---
# 지도를 클릭한 좌표를 기억하기 위한 저장소입니다.
if 'clicked_lat' not in st.session_state:
	st.session_state.clicked_lat = None
	st.session_state.clicked_lon = None


# 2. 데이터 로드
@st.cache_data
def load_data():
	PATH = "../data/pohang_location_202410.csv"
	df = pd.read_csv(PATH)
	return df


df_floating = load_data()

# 3. 사이드바 - 분석 설정
st.sidebar.header("분석 설정")
radius = st.sidebar.slider("분석 반경 (m)", 100, 500, 250)
show_grid = st.sidebar.checkbox("유동인구 그리드 표시 (전체)", value=False)  # 초기값은 꺼둠 (성능 고려)


# 4. 지도 생성 함수
def create_map(center_lat=36.019, center_lon=129.343, clicked_lat=None, clicked_lon=None):
	m = folium.Map(location=[center_lat, center_lon], zoom_start=14, tiles='cartodbpositron')

	if clicked_lat and clicked_lon:
		# 1. 클릭 지점 마커 및 반경 원 표시
		folium.Marker([clicked_lat, clicked_lon]).add_to(m)
		folium.Circle(
			location=[clicked_lat, clicked_lon],
			radius=radius,
			color='#3186cc',
			fill=True,
			fill_opacity=0.2
		).add_to(m)

		# 2. [핵심] 유동인구 체크박스가 켜져 있다면 '반경 내 데이터'만 격자로 표시
		if show_grid:
			# 반경 계산을 위한 거리 임계값 (이미 하단에서 계산한 nearby_df 활용)
			lat_degree_dist = radius / 111000
			lon_degree_dist = radius / 88000

			nearby_df = df_floating[
				((df_floating['lat'] - clicked_lat) ** 2 / lat_degree_dist ** 2 +
				 (df_floating['lon'] - clicked_lon) ** 2 / lon_degree_dist ** 2) <= 1
				]

			if not nearby_df.empty:
				# 컬러맵 생성 (반경 내 데이터의 최소/최대 기준)
				colormap = cm.LinearColormap(
					colors=['#FFD580', '#FF8C00', '#E31A1C', '#800026'],
					vmin=nearby_df['co'].min(),
					vmax=nearby_df['co'].max()
				).add_to(m)

				delta = 0.00025
				for _, row in nearby_df.iterrows():
					rect_bounds = [[row['lat'] - delta, row['lon'] - delta],
								   [row['lat'] + delta, row['lon'] + delta]]

					folium.Rectangle(
						bounds=rect_bounds,
						color=colormap(row['co']),
						fill=True,
						fill_color=colormap(row['co']),
						fill_opacity=0.6,
						weight=1,
						tooltip=f"인구: {int(row['co'])}명"
					).add_to(m)

	return m


# 5. 메인 지도 표시 및 렌더링
# 세션 상태에 저장된 클릭 좌표를 지도 생성 함수에 전달합니다.
m = create_map(clicked_lat=st.session_state.clicked_lat, clicked_lon=st.session_state.clicked_lon)
map_data = st_folium(
    m,
    width=900,
    height=600,
    key="pohang_analysis_map",
    returned_objects=["last_clicked"] # 클릭 데이터만 가져오도록 제한해서 부하 감소
)

# 6. 실시간 클릭 이벤트 감지 및 상태 업데이트
if map_data['last_clicked']:
	lat = map_data['last_clicked']['lat']
	lon = map_data['last_clicked']['lng']

	# 클릭한 좌표가 바뀌었을 때만 화면을 새로고침(rerun)하여 원을 그립니다.
	if lat != st.session_state.clicked_lat or lon != st.session_state.clicked_lon:
		st.session_state.clicked_lat = lat
		st.session_state.clicked_lon = lon
		#st.rerun()

# 7. 분석 결과 처리 (클릭된 좌표가 있을 때만 실행)
if st.session_state.clicked_lat and st.session_state.clicked_lon:
	c_lat = st.session_state.clicked_lat
	c_lon = st.session_state.clicked_lon

	st.subheader(f"선택 지점 분석 결과 (위도: {c_lat:.4f}, 경도: {c_lon:.4f})")

	# 반경 내 데이터 필터링 로직
	lat_degree_dist = radius / 111000
	lon_degree_dist = radius / 88000

	nearby_df = df_floating[
		((df_floating['lat'] - c_lat) ** 2 / lat_degree_dist ** 2 +
		 (df_floating['lon'] - c_lon) ** 2 / lon_degree_dist ** 2) <= 1
		]

	if not nearby_df.empty:
		avg_floating = nearby_df['co'].mean()
		max_floating = nearby_df['co'].max()
		total_points = len(nearby_df)

		col1, col2, col3 = st.columns(3)
		col1.metric("평균 유동인구", f"{int(avg_floating)}명")
		col2.metric("최대 밀집도", f"{int(max_floating)}명")
		col3.metric("분석 격자 수", f"{total_points}개")

		st.info(f"이 지역은 주로 **{nearby_df['ADMIN_DONG'].mode()[0]}** 인근에 위치해 있습니다.")
	else:
		st.warning("해당 반경 내에 유동인구 데이터가 존재하지 않습니다.")
else:
	st.write("지도를 클릭하면 해당 지점을 중심으로 반경 내 유동인구 분석이 시작됩니다.")

# 8. (보너스) 데이터 테이블 표시
if st.checkbox("전체 데이터 보기"):
	st.dataframe(df_floating.head(100))