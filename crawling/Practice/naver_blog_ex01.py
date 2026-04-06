import urllib.request
import datetime
import json
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
	pass

def getPostDate(post, jsonResult):
	pass

def main():
	jsonResult = []
	sNode = 'blog'
	search_text = '앤트로픽'
	display_count = 100

	jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
	while ((jsonSearch != None) and (jsonSearch['display'] != 0)):
		for post in jsonSearch['items']:
			getPostDate(post, jsonSearch)

		nStart = jsonSearch['start'] + jsonSearch['display']
		jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

	with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
		retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
		outfile.write(retJson)

	print('%s_naevr_%s.json SAVED' % (search_text, sNode))

if __name__ == '__main__':
	main()
