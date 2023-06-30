# 내장함수  range()
# end - range(10)
a=range(10)       # 0~9 1
print(a)               # range(0, 10)
print(list(a))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# start, and  - range(1, 10)
b=range(1, 10)
print(list(b))

# start, end, step  - range(1, 10, 2)
c=range(0, 11, 2)
print(list(c))

d=range(10, 0, -1)
print(list(d))
print("\n\n")

# 1~10 출력 for
"""
   for(let i=0;i<=10;i++){
      document.write(i + "<br>");
   }
"""

for i in range(1, 11, 1):
    print(i, end=' ')
print()

# 1~100까지의 짝수의 합
sum=0
for i in range(1, 101, 1):
    if i%2==0:
        sum +=i
print(sum)

# 2단 출력
dan=2
for i in range(1, 10, 1):
    print("%d * %d = %d" %(dan, i, dan*i))
print("\n\n")

"""
   for(let i=0;i<=10;i++){      // 1, 2
      for(let j=0;j<=5;j++){     // 12345
         document.write(i + ", " + j);
      }
   }
"""
for i in range(1, 4, 1):          # 1, 2, 3
    for j in range(1, 6, 1):      # 12345
        print("%d %d" %(i, j))
    print()
print()    

# 구구단 
for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print("%d*%d=%d" %(i, j, i*j))
    print()

print("\n\n=================")

#Collection for문
"""
   let arr=[1, 2, 3, 4, 5]
   for(let i=0;i<arr.length;i++){
      alert(arr[i])
   }
"""

# list
arr=[11, 12, 13, "apple", "banana", 25.7]
print(arr)
print(arr[0])

for value in arr:                      # 0, len(arr), 1
    print(value, end=' ')
print()

# set
su={1, 2, 3}
print(su)

for num in su:
    print(num, end=' ')
print()

# tuple
tup=(1, 2, 3)
print(tup, tup[0])
for val in tup:
    print(val, end=' ')
print()

# 5시 시작합니다.








