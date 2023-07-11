"""
   Queue :  FIFO (First in First Out)
   
   put() : eqQueue   저장 (rear)
   get() : deQueue    추출 (front)
"""

from queue import Queue

que=Queue()    # 가변길이 큐
que.put(66)           # eqQueue
que.put(77)
que.put(88)

print(que.qsize())
print(que.empty())
print(que.get())
print()

while not que.empty():
    print(que.get())

print(que.qsize())
print(que.empty())

print()

q=Queue()
q.put(91)
q.put(92)
q.put(93)
q.put(94)
q.put(95)
q.put(96)

print(q.queue[0])             # q[0]
print(q.queue[-1])
print()


# 내장함수
print(sum(q.queue))
print(max(q.queue))
print(min(q.queue))
print(len(q.queue))
