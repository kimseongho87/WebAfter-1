import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
import pandas as pd

# 왓챠사이트 접속
driver=webdriver.Chrome()
driver.get("https://pedia.watcha.com/ko-KR/contents/m53mZX3/comments")
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")

# 스파이더 리뷰
ultag=soup.find("ul", {"class":"css-10n5vg9-VisualUl ep5cwgq0"})
divtag=ultag.findAll("div", {"class":"css-1g78l7j"})

reviews=[]
for div in divtag:
    spantag=div.find("span")
    reviews.append(spantag.text)

# 스파이더맨 평점
divtag=soup.findAll("div", {"class":"css-yqs4xl"})

greades=[]
for div in divtag:
    spantag=div.findChildren()[1]
    greades.append(spantag.text)

driver.quit()
print(len(reviews))
print(len(greades))

# 데이터를 DataFrame으로 변환
data=pd.DataFrame({"Review":reviews, "Greade":greades})
print(data)

# 파일로 저장
path="C:\\Users\\JMH\\Desktop\\teacher\\workspace\\Python\\06_WebCrawler\\spiderMan.xlsx"
data.to_excel(path, index=False)


