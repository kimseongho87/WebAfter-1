# 백준 실습문제
import sys

n=int(input())   # 14

stack=[]
for i in range(1, n+1):
    std_input=sys.stdin.readline()       # 표준입출력에서 입력받아옴  push 1   
    cmd=std_input.rstrip().split()         # 오른쪽 공백 제거 후 공백으로 분리하여 리스트로 반환
  
    if cmd[0] == "push":
        stack.append(int(cmd[1]))

    elif cmd[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
         if len(stack) !=0:
             print(stack[-1])    
         else:
             print(-1)



    
