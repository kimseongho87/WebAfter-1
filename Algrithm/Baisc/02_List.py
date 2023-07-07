# List  자료형 : 생성, 추가, 삭제, 수정, 검색
# 함수의 시간복잡도  - O(1)
my_list=["apple", "banana", "사과", "딸기"]
print(my_list[3])               

my_list.append("melon")   # 맨마지막  
my_list.append("수박")
print(my_list)
print()

print(my_list.pop())            # 마지막 데이터는 출력하지만 list 삭제
print(my_list)
print()

# 함수의 시간복잡도 - O(n)   선형시간
a=[20, 27, 58, 72, 91]
a.insert(3, 0)
print(a)

del(a[3])
print(a)

print(a.index(72))

print(">>>>>>>>>>>>>>>>>>>>>")

import time
su=int(input("수:"))

num=[]
for i in range(su):        # 0, su, 1
   num.append(i)
# print(num)

start=time.time()
max_num=max(num)   
end=time.time() - start
print(max_num, "\t", end)       

"""
   결론 : 파이썬이 제공하는  기본 자료형으 해결되지 않은 것이 존재한다.  *** 자료 구조 필요
   프로그래머스, 백준, SW Expert Academy
"""