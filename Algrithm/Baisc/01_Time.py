"""
   시간복잡도 : 주어진 문제를 해결하기 위한 연산 횟수
                        일반적인 수행시간 1억번 연산 1초

                        O(1) < O(log n) < O(n log n)  < O(n^2)
"""

# O(1) : 입력값의 크기에 상관없이 실행시간 일정한 경우
arr=[10, 20, 30, 40, 50]
print(arr[0])
print(arr[-1])
print(arr[2])
print()

# O(log n) : 필요한 단계들이 연산마다 특정 요인에 의해 줄어 든다.
cnt=1
while cnt <=20:
    print(cnt)
    cnt=cnt * 2
print()

# O(n) : 주어진 n만큼 모두 데이터를 한번씩 처리한다. (선형의 시간)
for su in arr:     # [10, 20, 30, 40, 50]
    if su > 25:
        print(su)
print()

# O(n log n) : 데이터를 처하는데 O(n), 데이터를 반으로 나눈 과정 O(n log n)
for i in range(3):                # n번 반복
   j=1
   while(j <= 20):
        print("%d, %d"%(i, j))
        j=j*5                             # log n반복      
   print()                   
print()

# O(n^2)  : 이중 루프 (for, while), n^3 삼중 루프
for i in range(3):                # 0 1 2
    for j in range(5):            # 01234, 01234, 01234
        print("%d, %d"%(i, j))
    print()

