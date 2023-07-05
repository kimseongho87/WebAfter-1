# 파이썬 제공하는 표준 모듈 - 추가 설치 필요 없음

# math mudule : 수학 연산에 필요한 다양한 연산상수와 함수를 제공
import math                         # import math as m
result=math.pow(5, 3)          # 5^3
print(result, int(result))

from math import pow    #  from math import  *
print(pow(5, 3))

from math import pow as p
print(p(5, 3))
print()

print("제곱근:", math.sqrt(10), round(math.sqrt(10), 4))
print("x의 y승 (x^y):", math.pow(3, 2))
print("x의 계승 (5!):", math.factorial(5))
print("올림:", math.ceil(20.33))
print("내림:", math.floor(20.55))
print("소수이하 버림:", math.trunc(20.23), math.trunc(20.53))
print("절대값:", math.fabs(-20))
print("원주율 상수:", math.pi)
print()

# statistice module : 통계관련된 모듈
import statistics as sta
mylist=[10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
print("평균값:", sta.mean(mylist))
print("중앙값:", sta.median(mylist))
print("최빈값:", sta.mode(mylist))
print("모표준편차", sta.pstdev(mylist))
print("표준편차", sta.stdev(mylist))
print("분산:", sta.variance(mylist))
print()

# datetime, calendar 날짜 관련 모듈
import datetime
print("현재 날짜, 시간:", datetime.datetime.now())
print("현재 날짜:", datetime.date.today())

import calendar
print(calendar.calendar(2023))
print(calendar.month(2023, 7))
print(calendar.weekday(2023, 7, 5))     # 해당년월의 요일 출력 (0:월 ~~ 6:일)
print("\n\n")

# random  : 0 ~~ 1
import random
print(random.random())                # 0~1
print(random.randint(1, 10))         # 1~10 정수
print(random.uniform(1, 10))        # 1~10  실수
print()

nums=[1, 2, 3, 4, 5, 77, 88, 99]
print(random.choice(nums))

names=["최동윤", "백재웅", "안은비", "초채윤", "김명준", "박민수", "당현진", "한종악"]
print(random.choice(names))

random.shuffle(nums)
print(nums)

newnums=random.sample(nums, 3)
print(newnums)
print("\n\n")

# 로또 : 1~45, 6, 중복값 X
print("로또 >>>>>>>>>")
cnt=3
for i in range(cnt):                 # range(0, 3, 1)
   lotto=random.sample(range(1, 46), 6)
   print(lotto)


# 13분 시작합니다.   


