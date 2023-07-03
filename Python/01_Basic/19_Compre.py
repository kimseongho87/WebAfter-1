# Ex1)
arr=[1, 2, 3, 4, 5]
b=[]

for num in arr:
    num *= 3
    b.append(num)
print(b)

#  리스트 컴프리헨션으로 리스트에 3을 곱해서 새로운 리스트 생성
# [식 for 변수 in 리스트 if 조건식]
c=[num*3 for num in arr]         # c[0] 3, c[1] 6
print(c)
print("\n")

# Ex2)
arr=[1, 2, 3, 4, 5]
d=[]

for num in arr:
    if num%2==0:
        num*=3
        d.append(num)
print(arr)
print(d)

# 리스트 컴프리헨션  [식 for 변수 in 리스트 if 조건식]
x=[num*3 for num in arr if num%2==0]    # if문이 for문 뒤에 위치
print(x)
print("\n")

# Ex3)
arr=[1, 2, 3, 4, 5]
f=[]

for num in arr:
    if num > 2:
        num*=3
        f.append(num)
    else:
        f.append(0)
print(arr)
print(f)

# 리스트 컴프리헨션 if~else 문은 for문 앞에 위치
y=[num*3 if num > 2 else  0 for num in arr]
print(y)
print("\n")

# Ex4) Dictionary
dic={}
for num in range(1, 5, 1):
    dic[num]=num**2
print(dic, type(dic))

# Dictionary 컴프리헨션 
# {키:값 for 변수 in 딕셔너리 if 조건문}
mydic={num:num**2 for num in range(1, 5)}
print(mydic)
print("\n")

#Ex5) Set
mySet=set()
for num in range(1, 11, 1):
    if num%2 == 0:
        mySet.add(num)
print(mySet)

# 컴프리헨션 
# {식 for 변수 in  세트 if 조건문}
value={num for num in range(1, 11) if num%2==0}
print(value)