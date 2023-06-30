# 리스트 함수

# 추가
arr=[1, 2, 3]
arr.append(4)        # 리스트 끝에 새 요소를 추가
print(arr)

arr.insert(0, 77)      #  특정번지내에 요소를 추가
print(arr)

arr.insert(2, 88)
print(arr)

# 정렬
arr.sort()                     # 오름차순: 123456 abcde 가나다              내림차순: 654321 ~~~
print(arr)

arr.reverse()
print(arr)
print("\n\n")

# 삭제
car=['BMW', "BENZ", "VOVLO", "AUDI"]
print(car.index("BMW"))
print(car[0])

car.remove("BMW")        #   ["BENZ", "VOVLO", "AUDI"]
del car[1]                         #   ["BENZ", "AUDI"]     
print()

# 리스트 리스트 추가 하는 함수
num=[10, 20, 30]
value=[40, 50, 60]
num.extend(value)              # [10, 20, 30, 40, 50, 60]]
num.extend(["apple", "banana", "melon"])
print(num)                           #   [10, 20, 30, 40, 50, 60, 'apple', 'banana', 'melon']
r=num[3]
print(r)
print(num)
print("\n")


# 나중에 자료구조 - 고정 stack
su=[1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
print(su)
print(su.count(1))                # 3
val=su.pop()                        # 맨 마지막 요소 출력 후 삭제
print(val)
print(su)
print()

# 내장함수 
a="apple"
b=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(a))
print(len(b))
print(max(b), min(b))
print(max(a), min(a))

print(sorted(b))
print(sorted(a), type(sorted(a)))

# 연산자 in, not in
print(4 in b)
print(4 not in b)



 
