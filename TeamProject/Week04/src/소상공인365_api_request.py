import requests
import pandas as pd
import time
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import *
from IPython.display import HTML, display
import webbrowser
import requests

# 'Network' 탭의 'Headers'에서 확인한 진짜 주소 (예시입니다)
data_url = "https://bigdata.sbiz.or.kr/api/getSpecificRegionSales.do"

# 브라우저가 보내는 것과 똑같은 설정값을 넣어줘야 '거부'당하지 않습니다.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    # 한글이 포함된 헤더는 일단 과감히 주석 처리하거나 지워보세요.
    # "Some-Header": "한글값"
}

# 클릭했을 때 서버로 날아갔던 파라미터 (예: 행정동 코드, 좌표 등)
params = {
    "admCd": "47113...",
    "certKey": API_BUSINESS_KEY
}

response = requests.get(data_url, headers=headers, params=params)
data = response.json()

# 이제 'data' 변수에 매출 정보가 숫자로 들어와 있습니다!
print(data['total_sales'])
