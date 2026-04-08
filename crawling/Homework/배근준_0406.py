import urllib.request
import datetime
import json
import pandas as pd
import csv
from config import *

def get_request_url(url):
	req = urllib.request.Request(url)
	req.add_header("X-Naver-Client-Id", client_id)
	req.add_header("X-Naver-Client-Secret", client_secret)
	try:
		response = urllib.request.urlopen(req)
		if response.getcode() == 200:
			print("[%s] Url Request Success" % datetime.datetime.now())
			return response.read().decode('utf-8')
	except Exception as e:
		print(e)
		print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
		return None

def getNaverSearchResult(sNode, search_text, page_start, display):
	base = "https://openapi.naver.com/v1/search"
	node = "/%s.json" % sNode
	# urllib.parse.quote(): 문자나 한글 같은 유니코드 문자열을 퍼센트 인코딩(Percent-encoding)하여 URL로 반환하는 함수
	parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)

	url = base + node + parameters

	retData = get_request_url(url)
	print(retData)
	if (retData == None):
		return None
	else:
		# json.loads(): JSON 형식의 문자열(String)을 파이썬 객체(딕셔너리나 리스트)로 반환하는 함수
		return json.loads(retData)

def getPostData(post, lstResult):
	title = post['title']
	originallink = post['originallink']
	link = post['link']
	description = post['description']
	pubDate = post['pubDate']

	#jsonResult.append({'title': title, 'originallink': originallink, 'link': link, 'description': description, 'pubDate': pubDate})
	lstResult.append([title, originallink, link, description, pubDate])

	return

def main():
	lstResult = []
	sNode = 'news'
	search_text = input("검색 키워드 입력 => ").strip()
	display_count = 100

	jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
	if ((jsonSearch != None) and (jsonSearch['display'] != 0)):
		for post in jsonSearch['items']:
			getPostData(post, lstResult)

	# with open('%s_naver.csv' % search_text, 'w', encoding='utf8') as outfile:
	# 	retJson = json.dumps(lstResult, indent=4, sort_keys=True, ensure_ascii=False)
	# 	outfile.write(retJson)

	news_tbl = pd.DataFrame(lstResult, columns=('title', 'originallink', 'link', 'description', 'pubDate'))
	news_tbl.to_csv(search_text + "_naver.csv", encoding="utf8", mode="w", index=False, quoting=csv.QUOTE_ALL)

	print('%s_naver.csv SAVED' % search_text)

if __name__ == '__main__':
	main()
