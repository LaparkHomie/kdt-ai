import requests
import pandas as pd
import time
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import *


def collect_full_data(start_month_str, num_months=12):
	url = "https://apis.data.go.kr/5020000/pohangDynmcPopltnMtAccto/getPohangDynmcPopltnMtAccto"

	if not os.path.exists('pohang_data'):
		os.makedirs('pohang_data')

	# 시작 달 설정 (ex: '202410')
	current_date = datetime.strptime(start_month_str, "%Y%m")

	for _ in range(num_months):
		period = current_date.strftime("%Y%m")
		month_items = []
		page = 1

		print("--- %s 포항 전 지역 데이터 수집 시작 ---" % period)

		while True:
			params = {
				'serviceKey': FLOATING_POPULATION_API_KEY,
				'pageNo': str(page),
				'numOfRows': '1000',
				'type': 'json',
				'ym': period
			}

			try:
				response = requests.get(url, params=params)
				if response.status_code == 200:
					data = response.json()

					# 데이터 존재 여부 확인
					body = data.get('response', {}).get('body', {})
					items_container = body.get('items')

					if items_container and 'item' in items_container:
						items = items_container['item']
						month_items.extend(items)
						print("[%s] %d 페이지 수집 중..." % (period, page))

						if len(month_items) >= int(body.get('totalCount', 0)):
							break
						page += 1
					else:
						print("%s 데이터 수집 완료 또는 데이터 없음." % period)
						break

				time.sleep(0.1)
			except Exception as e:
				print("에러 발생: " + e)
				break

		if month_items:
			df = pd.DataFrame(month_items)
			# 중복 좌표 제거 (혹시 모를 API 중복 방지)
			df = df.drop_duplicates(subset=['xcnts', 'ydnts'])
			filename = "../raw/floating/pohang_%s.csv" % period
			df.to_csv(filename, index=False, encoding="utf-8-sig")
			print("저장 완료: " + filename)

		# 한 달 전으로 이동
		current_date -= relativedelta(months=1)


if __name__ == "__main__":
	# 최근 데이터가 있는 2024년 10월부터 역순으로 2개월치 수집
	collect_full_data('202410', num_months=2)
