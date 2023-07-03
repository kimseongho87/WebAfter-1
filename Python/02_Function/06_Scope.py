# 변수 유효 범위 : 지역변수, 전역변수
# Ex1)
a="전역변수"

def sub():
    b="지역변수"
    print(b)
    print(a)

sub()
print(a)
# print(b)     ERROR
print("\n")

#Ex2)
def fun(x):         # 매개변수는 지역에서만 사용
    print(x)

    global y          # 선언후 해당변수에 값 대입
    y="전역변수"

    print(y)

fun("매개변수")  
print(y)
