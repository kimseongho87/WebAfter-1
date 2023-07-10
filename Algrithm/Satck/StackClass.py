# list - append() / pop(), print(stack[-1]) / len(stack) /  len(stack) == 0

class Stack:
    def __init__(self):          # 스택객체 생성
        self.items=[]

    def push(self, data):                  # 스택 요소 추가 
         self.items.append(data)
      
    def pop(self):                             # 맨뒤 요소 삭제하고 리턴
        return self.items.pop()
    
    def peek(self):                            # 맨뒤 요소 리턴    
        return self.items[-1]
    
    def size(self):                             # 스택 사이즈
        return len(self.items)
    
    def isEmpty(self):                       # 비었는지 확인 true           
         return not self.items    
    

if __name__ == "__main__":
    stack=Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print(stack.size())
    print(stack.pop())
    print(stack.size())

    print(stack.peek())
    print(stack.size())
    print(stack.isEmpty())

    # 3시 1분