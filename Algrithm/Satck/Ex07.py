# 고정 길이 스택 - 동적(가변)/고정

# push
stack=[None] * 5
print(stack)
stack.append(12)
print(stack)
stack.append(13)
print(stack)
print()

stack=[None] * 10
print(stack)
top=-1

top +=1                   # 0
stack[top]="커피"    # stack[0]="커피"

top +=1                    # 1
stack[top]="녹차"      # stack[1]="녹차"  

top +=1                     # 2
stack[top]="꿀물"      # stack[2]=꿀물

slen=len(stack)
print("%d %d \n"%(top, slen))

for i in range(slen-1, -1, -1):         # (9 ~ 0 , -1)
   print(stack[i])

print()

# pop
print("%d %d \n"%(top, slen))
data=stack[top]              # stack[2]
stack[top]=None
top -=1
print(data)

data=stack[top]                 # stack[1]
stack[top]=None
top-=1
print(data)

data=stack[top]
stack[top]=None
top -=1
print(data)
print()

for i in range(slen-1, -1, -1):
   print(stack[i])


   # 50분 시작
