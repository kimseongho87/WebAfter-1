# 웹 서핑에서 이전 페이지 돌아가기

import webbrowser
import time
from StackClass import Stack

stack=Stack()
urls=["naver.com", 'daum.net', "nate.com"]

# push
for url in urls:
    stack.push(url)
    webbrowser.open("http://" + url)
    print(url, end="push ----------->")
    time.sleep(3)

print("방문종료")
time.sleep(5)

# pop
while True:
    url=stack.pop()
    webbrowser.open("http://" + url)
    print(url, end="pop -------------->")

    if stack.size() == 0 :
        break
    
    time.sleep(5)

print("방문종료")

# 4시 시작합니다.
