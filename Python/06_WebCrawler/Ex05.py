import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
import pandas as pd
import time

# 왓챠사이트 접속
driver=webdriver.Chrome()
driver.get("https://pedia.watcha.com/ko-KR/contents/md71bBW/comments")

# 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight") 
    if new_height == last_height:
        break
    last_height = new_height     

html=driver.page_source
soup=BeautifulSoup(html, "html.parser")

# 인디어나 존슨  평점
divtag=soup.findAll("div", {"class":"css-yqs4xl"})

greades=[]
for div in divtag:
    spantag=div.findChildren()[1]
    greades.append(spantag.text)

driver.quit()
print(len(greades))

# 데이터를 DataFrame으로 변환
data=pd.DataFrame({"Greade":greades})
print(data)

# 파일로 저장
path="C:\\Users\\JMH\\Desktop\\teacher\\workspace\\Python\\06_WebCrawler\\movie.xlsx"
data.to_excel(path, index=False)

# 16분 시작


