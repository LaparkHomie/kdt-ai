from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def bugs(result, date):
	rank = 0
	bugs_url = "https://music.bugs.co.kr/chart/track/day/total?chartdate=" + date
	html = urllib.request.urlopen(bugs_url)
	soupBugs = BeautifulSoup(html, 'html.parser')

	tblBugs = soupBugs.tbody
	for musicinfo in tblBugs.select("tr"):
		rank = rank + 1
		artist = musicinfo.select("td > p.artist > a")[0].string
		title = musicinfo.select("th > p.title > a")[0].string
		# title = musicinfo.th.p.a.string 이렇게 해도되지만, 정석적인 방법으로 사용

		result.append([date, rank, artist, title])

def main():
	result = []
	date = input("순위 검색할 날짜를 8자리로 입력하세요!!(ex : 20060922~현재날짜 사이 입력) => ")
	bugs(result, date)

	bugs_tbl = pd.DataFrame(result, columns=('입력날짜(search_day)', '랭킹(rank)', '아티스트(singer)', '곡타이틀(title)'))
	bugs_tbl.to_csv("bugchart_" + date + ".csv", encoding="utf8", mode="w", index=False)
	del result[:]

if __name__ == "__main__":
	main()
