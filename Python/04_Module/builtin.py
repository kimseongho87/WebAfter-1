# 내장함수 :  점 . 연산 (클래스, 모듈), print(), input() 명 사용

print("절대값:", abs(1))
print("절대값:", abs(-3.5))
print("아스키 코드:", chr(97), chr(65))
print()

print(dir(list))
print(dir([1, 2, 3, 4, 5]))
print(dir(dict))
print(dir({'1':'a'}))
print()

print(5//2)
print(5%2)
print("몫과 나머지", divmod(5, 2))
# a, b=5//2, 5%2


# enumerate 인덱스 값을 포함 데이터를 반환
arr=[10, 20, 30, 40, 50]

for val in arr:
    print(val, end=" ")
print()

for idx, val in  enumerate(arr):
    print(idx, val)
print()    

# eval() 
print("1+2")
print(eval("1+2"))
print()

# int()
print(int('3'))
print(int(3.14))
print(int(10))
print()

# len()
print(len("Hello"))
print(len([1, 2, 3, 4, 5]))
print()

#min(), max()
print(max([1, 2, 3, 4, 5, 6, 77, 88, 0]))
print(min("Hello"))       # a 97,  A 65
print(min("hello"))  
print()

# round
print(round(5.56))
print(round(5.56, 1))
print()

# isinstacne : 해당 클래스에서 만들어진 객체인가?
class Person:
    pass

p=Person()
print(isinstance(p, Person))