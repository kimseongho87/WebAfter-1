# 고정길이 큐 - List 활용해서 만듬

# enQueue, rear - 저장
que=[None]*5
front=rear=-1

print(front, rear)

rear += 1
que[rear]="화사"
print(front, rear)

rear +=1
que[rear]="솔라"
print(front, rear)

rear +=1
que[rear]="문별"
print(front, rear)

for i in range(len(que)):
    print(que[i], end=' ')
print("\n============ \n")

# deQueue 

front +=1
data=que[front]
que[front]=None
print(data)
print(front, rear)

front +=1
data=que[front]
que[front]=None
print(data)
print(front, rear)

front +=1
data=que[front]
que[front]=None
print(data)
print(front, rear)

for i in range(len(que)):
    print(que[i], end=' ')


# 1시에 시작합니다.
