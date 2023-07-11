from StackFixed import Stack

# list append() / pop() / [-1]
stack=Stack(5)     # push() 저장, pop() 추출, peek() 출력
stack.push(77)
stack.push(88)
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.push(77)
stack.push(88)
stack.push(77)
stack.push(88)
stack.push(77)
stack.push(88)