# 반복문
sum=0
for n in range(10, 0, -1):
    sum +=n
print("sum:", sum)

# 재귀함수
def add(num):        #   5  4 3 2 1
    if num <=1:
        return 1
    
    return num + add(num-1)    #   num:5    add(4) / num:4   add(3) / num:3 add(2)  / num:2  add(1)

print(add(10))


