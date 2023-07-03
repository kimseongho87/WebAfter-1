# CASE-2) 인수:O, 리턴:X
# Ex1)
def sum(a, b):
    print(a+b)

sum(10, 20)
sum(55.5, 66.6)
print()

# Ex2)
def sub(a):
    for i in range(1, a):
        print("*", end="")
    print()

sub(5)
sub(10)
sub(3)
print("\n")

# Ex3)
def hap(su, value):
    print(su + value)

def cha(su, value):
   print(su - value)       

def mul(su, value):
    print(su * value)

def div(su, value):
    print(su / value)


first=int(input("수:"))
second=int(input("수:"))

hap(first, second)
cha(first, second)
mul(first, second)
div(first, second)
print()

# Ex4)  python 모든 자료의 인수/매개변수 처리가 쉽다 / 정수, 실수, 문자열, list, tuple, set, dic
def apple(a):
    print(a, type(a))

apple(10)
apple(55.5)
apple("A")
apple('멀티캠퍼스')
apple([1, 2, 3])
apple((77, 88, 99))
apple({"apple":"사과", "banana":"바나나"})
apple({'A', 'B', 'C'})


