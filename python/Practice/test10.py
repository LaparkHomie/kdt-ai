# # datetime.data() : 연, 월, 일로 날짜를 표현할 때 사용하는 함수
# import datetime
#
# day = datetime.date(2021, 12, 14)
# print(day)
# print(day.weekday())
#
# # time.time() : UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 변환하는 함수
# # 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환
# import time
# print(time.time())
#
# # time.localtime() : time.time()이 반환한 실숫값을 연, 월, 일, 시, 분, 초, ... 형태로 바꾸어 주는 함수
# print(time.localtime())
#
# # time.strftime() : 시간에 관계된 것들을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
# import time
#
# print(time.strftime('%x', time.localtime(time.time())))
# print(time.strftime('%c', time.localtime(time.time())))
# print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#
# # datetime 클래스 : 날짜와 시간을 동시에 표현하기 위해서 사용되며,
# # 위에서 다른 date와 time 클래스에서 지원하는 대부분의 기능을 지원
# from datetime import datetime
#
# now = datetime.now()
# print("현재 날짜와 시간:", now)
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print("포맷된 날짜와 시간:",  formatted_date)
# print("%s년 %s월 %s일 %s시 %s분 %s초" % (now.year, now.month, now.day, now.hour, now.minute, now.second))
#
# print(datetime(2026 , 3, 8, 10, 10, 10))
#
# # random 모듈 : 난수(규치깅 없는 수)를 발생시키는 모
# # random 함수 : 0부터 1 사이의 랜덤 실수를
# # uniform() 함수 : 2개의 숫자 사이의 랜덤 실수를 반환한다.
# # randint() 함수 : 2개의 숫자 사이의 랜덤 정수를 반환한다. (2번째 인자로 넘어온 정수도 범위도 포함시킴)
# # choice() 함수 : 랜덤하게 하나의 원소를 선택한다.
# # sample() 함수 : 랜덤하게 여러 개의 원소를 생성한다.
# # shuffle() 함수 : 원소의 순서를 랜덤하게 변경한다.
# import random
#
# print(random.random()) # 0과 1 사이 난수 생성
# print('1.---------------------------')
# print(random.uniform(1, 10)) # 1과 10 사이의 난수 생성
# print('2.---------------------------')
# print(random.randint(1, 10)) # 1부터 10 사이의 정수형 난수 반환
# print('3.---------------------------')
# print(random.randrange(0, 100, 2)) # 0부터 100사이 짝수중(2증가) 하나 선택
# print('4.---------------------------')
# print(random.choice('acdefghij')) #
# print('5.---------------------------')
# print(random.sample([1, 2, 3, 4, 5], 3))
# print('6.---------------------------')
# items = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(items)
# print(items)

# # os 모듈 : 운영체제에서 제공하는 정보를 제공하거나 운영체제의 기능을 사용할 수 있는 방법을 제공
import os
#
# print(os.name) # 사용자 이름
print(os.getcwd()) # 프로젝트 위치
# print(os.path.join(os.getcwd(), "test")) # 프로젝트 위치 + 폴더 추가
# os.mkdir(os.path.join(os.getcwd(), "test")) # 파일 생성

# os.rmdir(os.path.join(os.getcwd(), "test"))
# os.remove(os.path.join(os.getcwd(), "test.py"))

os.chdir("C:\\Windows") # 경로를 변경하라
os.chdir("C:\\Users\\NT371B5A\\Documents\\Project\\Python\\kdt-python-study\\python\\Practice") # 경로를 변경하라
print(os.getcwd())
print(os.listdir())
