# 고정길이 stack 

class Stack:
    def __init__(self, size):   # 2
        self.size=size
        self.stack=[None] * size
        self.top=-1
       # print( self.stack)

      # push() 때문에 꽉찼니?
    def is_full(self):
         return self.top == self.size-1
        
    def push(self, data):
        if self.is_full():     # True
            print("스택이 가득 차 있습니다.")
            return 
        self.top +=1
        self.stack[self.top]=data

   # pop() 때문에 비어있니?
    def is_Empty(self):
        return self.top == -1
    
    def pop(self):
        if self.is_Empty():
            print("스택이 비어 있습니다.")
            return 
   
        data=self.stack[self.top]
        self.top -=1
        return data 
     
    def peek(self):
       if self.is_Empty():
           print("스택이  비어 있습니다.")
           return 
       return self.stack[self.top]
