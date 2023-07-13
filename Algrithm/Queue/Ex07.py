from QueueClass import Queue

def remove_duplicates(queue):
   myset=set()
   newque=Queue(queue.size)

   while not queue.is_empty():
      item=queue.dequeue()
      if item not in myset:
         myset.add(item)
         newque.eqqueue(item)
   return newque

# 4시 5분
if __name__ == "__main__":
   queue = Queue(7)
   queue.eqqueue(1)
   queue.eqqueue(3)
   queue.eqqueue(2)
   queue.eqqueue(3)
   queue.eqqueue(4)
   queue.eqqueue(2)
   queue.eqqueue(5)

   newque=remove_duplicates(queue)
   while not newque.is_empty():
      print(newque.dequeue(), end=' ')