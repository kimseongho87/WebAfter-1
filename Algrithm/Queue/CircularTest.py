from CircularClass import Circular

que=Circular(5)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
print()

que.dequeue()
que.dequeue()
que.enqueue(77)
que.enqueue(88)
que.enqueue(99)

que.dequeue()
que.dequeue()
que.dequeue()
print(que.peek())
