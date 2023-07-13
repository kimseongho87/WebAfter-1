# 고정길이 큐

class Queue:
    def __init__(self, size):
        self.size=size
        self.queue=[None]*size
        self.rear=self.front=-1

    # 저장
   #  def is_full(self):
   #      return self.rear == self.size-1
    
    # 저장, 데이터 이동
    def is_full(self):
         if self.rear != self.size-1:        # 뒤에 있는 상태
            return False

         elif self.rear==self.size-1 and self.front==-1:         # 꽉찬 상태
             return True
         
         else:               # 데이터 이동 후 추가 가능한 상태 rear=size-1, front !=-1
             print(self.front, self.rear)    # 0 4
             
             for i in range(self.front+1, self.size):  # 1 2 3
                 self.queue[i-1]=self.queue[i]        # [0]  11 = [1] 11
                 self.queue[i]=None                      # [1] = None

             self.front-=1
             self.rear-=1
             return False

    def eqqueue(self, data):     # 10 
        if self.is_full():
            print("큐가 꽉찼습니다.")
            return 
        
        self.rear +=1
        self.queue[self.rear]=data
        print(self.queue, self.front, self.rear)

    # 추출 (삭제 포함) 
    def is_empty(self):
        return self.front==self.rear
    
    def dequeue(self):
        if self.is_empty():
            print("큐가 비어 있습니다.")
            return 
        
        self.front +=1
        data=self.queue[self.front]
        self.queue[self.front]=None
        print(self.queue, self.front, self.rear)

        return data
    
    # 출력
    def peek(self):
        if self.is_empty():
            print("큐가 비어 있습니다.")
            return 
        
        return self.queue[self.front +1]
    

 
