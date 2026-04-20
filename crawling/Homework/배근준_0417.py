from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

query = input("검색 키워드 입력 : ")
lst_blog = []

driver = webdriver.Chrome()
driver.get('https://www.naver.co.kr/')
time.sleep(3)

search_box = driver.find_element(By.ID, "query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[5]/a').click()
time.sleep(1)

html = driver.page_source
soupCB = BeautifulSoup(html, 'html.parser')
all_blog = soupCB.select("a.fender-ui_228e3bd1.T4d_tSMrB8qRjbb9_yER")

for blog in all_blog:
	lst_blog.append((blog.text, blog.get("href")))

driver.quit()

for blog in lst_blog:
	print("제목: " + blog[0])
	print("링크: " + blog[1])
	print("--------------------------------")

CB_tbl = pd.DataFrame(lst_blog, columns=('제목', '링크'))
CB_tbl.to_csv('naver_%s.csv' % query, encoding='utf-8', mode='w', index=False)
