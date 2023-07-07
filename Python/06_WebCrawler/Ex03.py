"""
   영화 스파이더맨 리뷰 - 1page 8개
   과정 : 스크롤 동적 - 리뷰, 별점 - csv 파일 저장 - 데이터분석, 그래프
   설정 : pip install selenium - 자동화 처리
             chromedriver  (VS: 114.0.5735.199)

             이미지 검색 - 저장
""" 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
import urllib.parse

# 웹 드라이버 초기화
driver=webdriver.Chrome()

# 구글 - 이미지 - 검색어 입력 
driver.get("https://www.google.com/imghp?hl=ko&tab=ri&ogbl")
elem=driver.find_element(By.NAME, "q")
elem.send_keys("펭수")
elem.submit()

# 스크롤 추가
# Get scroll height  끝
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom    처음~끝, 끝까지 스크롤을 내리겠다
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page   로딩시간
    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")     # 현재
    if new_height == last_height:       # 현재 == 끝
        break
    last_height = new_height              # 스크롤이 길어지면
  

time.sleep(2)
images=driver.find_elements(By.CLASS_NAME, "rg_i.Q4LuWd")
print("이미지 갯수>>>>>", len(images))

# 이미지 다운
path="C:\\Users\\JMH\Desktop\\teacher\\workspace\\Python\\06_WebCrawler\\images\\"

count=1
for img in images:
    src=img.get_attribute("src")
    try:
         urllib.request.urlretrieve(src, path+str(count)+".jpg")
         count=count + 1
    except Exception :
         print("다운로드 불가")       

# 웹 드라이버 닫기
driver.quit()

