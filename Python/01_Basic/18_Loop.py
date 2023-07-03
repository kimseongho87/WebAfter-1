# break :  반복문에서 break 문장을 만나면 반복문 빠져나감
for i in range(1, 11, 1):
    if i==5:
        break
    print(i, end=' ')
print()

cnt=1
while cnt <=10:
    if cnt==5:
      break
    print(cnt, end=' ')
    cnt=cnt+1
print()

# continue : 반복문에서 continue 반복을 빠져나가지 않고 그다음 순서(맨 처음 조건으로 돌아감)
for i in range(1, 11, 1):     # range(1, 11):  range(11):
    if i==5:
        continue
    print(i, end=' ')
print()

cnt=0
while cnt <=10:
    cnt=cnt+1
    if cnt==5:
      continue
    print(cnt, end=' ')
print()

# 실습문제 - 커피가 10잔(1잔 10원), 돈 300
coffee=10
money=300

while True:
    coffee=coffee-1
    money=money-10

    if coffee==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
    if money < 10:
        print("돈이 다 떨어졌습니다")
        break
    
    print("커피를 제공합니다. 남은 %d, 남은 커피는 %d"%(money, coffee))


