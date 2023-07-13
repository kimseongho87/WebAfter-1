from queue import Queue

n=int(input())          # 1234  342 24
cards=Queue()

# 저장  
for num in range(1, n+1):
    cards.put(num)
   # print(cards.get())

# 추출
while cards.qsize() > 1:
    cards.get()     # 1
    cards.put(cards.get())     # 2

print(cards.get())

# 10분 시작
