# 제어문 - 반복문
# 1~5 출력
su=1
while su <=5:
    print(su, end=' ')
    su+=1
print()

# 1~10 까지의 숫자 중 홀수만 출력
num=1
while num <= 10:
      if num%2==0:
               print(num, end=' ')
      num +=1
print()

# 1~100 합
sum=0
i=1
while i <=100:
      sum +=i
      i +=1
print(sum)