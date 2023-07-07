# Ex1)
b=[]
arr=[1, 2, -3, 4, 5]
for num in arr:
    num *=3
    b.append(num)
print(b)

# 식 for 변수 in 리스트 if 조건
c=[num*3 for num in arr]
print(c)
print()

# Ex2) 
c=[]
for num in arr:
   if num%2==0:
       num*=3
       c.append(num)
print(c)

d=[num*3 for num in arr if num%2==0]
print(d)
print()

# Ex3)
x=[]
for num in arr:
    if num > 0:
        num*=3
    else:
         num=0

    x.append(num)
print(x)

y=[num*3 if num > 0 else 0 for num in arr]
print(y)