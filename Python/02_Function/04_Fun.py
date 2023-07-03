# Python 함수 : 키워드 인수, 기본값 인수, 가변 인수, 키워드 가변 인수
# 1) 키워드 함수 : 인수의 개수가 많을때 순서를 알기 어렵고, 전달시 위치를 헷갈려 할 수 있다 

def hap(a, b):
    print("a=%d, b=%d"%(a, b))
    return a+b

print(hap(10, 20))                        # 위치 인수
print(hap(a=55, b=66))               # 키워드 인수
print(hap(b=1, a=2))
print(hap(100, b=200))
# print(hap(a=99, 88))                 ERROR  키워드 인수가 위치 인수 전에 나올 수없다
print("\n")

# 2) 기본값(default) 인수 : 인수 값을 전달하지 않을 경우, 자주 바꾸지 않은 데이터는 기본값으로 처리
# Ex1)
def sum(a, b=1, c=2):
    print("a=%d, b=%d, c=%d"%(a, b, c))
    return a+b+c

print(sum(10))
print(sum(66, 77, 88))

def abc(x=1, y=2, z=3):
    pass

# def xyz(a=1, b, c=10):   ERROR
#     pass

# Ex2)
def calc(begin, end, step=1):
    sum=0
    for n in range(begin, end+1, step):
        sum +=n
    return sum

print(calc(1, 10))
print(calc(5, 50))
print(calc(1, 10, 2))
