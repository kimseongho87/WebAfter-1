from QueueClass import Queue

def my_max(que):
    max_value=que.dequeue()
    while not que.is_empty():
        item=que.dequeue()
        if item > max_value:
            max_value=item
    return max_value

def my_sum(que):
    hap=0
    while not que.is_empty():
        hap +=que.dequeue()
    return hap

if __name__ == "__main__":
   que=Queue(5)
   que.eqqueue(5)
   que.eqqueue(2)
   que.eqqueue(80)
   que.eqqueue(1)
   que.eqqueue(10)
   print()

   print(my_max(que))
   # print(my_sum(que))