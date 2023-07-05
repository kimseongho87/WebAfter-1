import requests
from bs4 import BeautifulSoup 

# 스파이더맨 리뷰
def watcha_movie():
    req=requests.get("https://pedia.watcha.com/ko-KR/contents/m53mZX3/comments")
    html=req.text
    # print(html)

    soup=BeautifulSoup(html, "html.parser")
    ultag=soup.find("ul", {"class":"css-10n5vg9-VisualUl ep5cwgq0"})
    divtag=ultag.findAll("div", {"class":"css-1g78l7j"})
   # divtag=soup.findAll("div", {"class":"css-1g78l7j"})
   # print(len(divtag))
    
    count=0
    for div in divtag:
        count +=1
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", count)
        spantag=div.find("span")
        print(spantag.text)
    
# 스파이더맨 평점
def  watcha_grade():
    req=requests.get("https://pedia.watcha.com/ko-KR/contents/m53mZX3/comments")
    html=req.text

    soup=BeautifulSoup(html, "html.parser")
    divtag=soup.findAll("div", {"class":"css-yqs4xl"})
    # print(len(divtag))
    for div in divtag:
        #  spantag=div.find("span")
        spantag=div.findChildren()[1]
        print(spantag.text)

if __name__ == "__main__":
   # watcha_movie()
    watcha_grade()


    # 5시 7분 시작