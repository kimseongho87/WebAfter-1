# CASE-3) 인수:X, 리턴:O
# Ex1)
def name():
    return "제이름은 펭수입니다"

irum=name()
print(irum)

# Ex2)
def sub1():
   return 10

def sub2():
    return 24.4

def sub3():
    return [1, 2, 3, 4]

def sub4():
    return "apple"

def sub5():
    return {"a":"apple", "b":"banana"}

print(sub1())

su=sub2()
print(su, type(su))

print(sub3())
print(sub4())
print(sub5())
print()

# CASE-4) 인수:O, 리턴:O
# Ex1)
def add(a, b):
    return a+b

c=add(1, 2)
print(c)

# Ex2)
def total(kor, eng, mat):
    return kor+eng+mat

def average(tot):
    return tot // 3

tot=total(80, 90, 85)
avg=average(tot)
print("홍길동 점수는 %d %d"%(tot, avg))
print()

# CASE-5) 인수:O, 리턴:O (리턴값이 여러개 존재)
def swap(a, b):     # 10, 77
    return b, a        # 77 10

c, d=swap(10, 77)
print(c)
print(d)