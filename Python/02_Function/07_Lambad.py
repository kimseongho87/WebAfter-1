# 람다함수 == 익명함수
# lambda 매개변수... : 매개변수 표현식
# Ex1)
def add(x, y):
    return x+y

r=add(1, 2)
print(r)

hap=lambda x, y : x+y
print(hap(10, 20))
print()

# Ex2)
def mul(x):
    return x*2

e=mul(10)
print(e)

m=lambda x : x*2
print(m(33))
print("\n")

# map() 함수 : 각 요소에 대해 지정한 함수를 새로운 List(객체)를 생성하여 반환 
# Ex1)
def list_mul(num):
    print(num)
    
    arr=[]
    for val in num:
        arr.append(val * 2)
    return arr
    
print(list_mul([1, 2, 3, 4, 5]))
print()

numbers=[1, 2, 3, 4, 5]
my_list=map(lambda x : x*2, numbers)
print(list(my_list))
print()

# Ex2)
def list_str(strings):
    print(strings)

    upstrings=[]
    for s in strings:
        upstrings.append(s.upper())
    return upstrings

print(list_str(["apple", "banana", "cherry"]))

strings=["apple", "banana", "cherry"]
upper_str=map(lambda s: s.upper(), strings)
print(list(upper_str))
print()

# filter() 함수 : 특정 조건을 만족하는 값들만 추출하여 반환
numbers=[1, 2, 3, 4, 5]
odd_numbers=filter(lambda x: x % 2 !=0, numbers)
print(list(odd_numbers))

def list_odd(num):
    print(num)

    arr=[]
    for su in num:
        if su%2 !=0:
            arr.append(su)

    return arr

print(list_odd(numbers))


