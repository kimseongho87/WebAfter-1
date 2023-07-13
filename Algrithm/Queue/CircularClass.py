class Circular:
    def __init__(self, size):
        self.size=size
        self.que=[None]*self.size
        self.fornt=self.rear=0    

    # 저장
    def is_full(self):
        return (self.rear+1)%self.size == self.fornt       # 01234 01234


    def enqueue(self, data):
         if self.is_full():
             print("큐가 꽉 찼습니다.")
             return 
         
         self.rear=(self.rear+1) % self.size                # 01234  01234
         self.que[self.rear]=data
         print(self.que)

      # 추출
    def is_empty(self):
        return self.fornt==self.rear
    
    def dequeue(self):
        if self.is_empty():
            print("큐가 비어 있습니다.")
            return 
        
        self.fornt=(self.fornt+1) % self.size
        data=self.que[self.fornt]
        self.que[self.fornt]=None
        print(self.que)
        return data
    
    # 출력
    def peek(self):
        if self.is_empty():
            print("큐가 비어 있습니다")
            return 
        return self.que[(self.fornt+1) % self.size]



