# 3) 가변 인수 - 여러개(n) 전달해서 처리하고 싶을때
def abc(*value):
    print(value, type(value))

abc(100)    
abc(1, 2)
abc(6, 7, 8, 9, 10)
print()

def calc(num, *values):
    print(num, values)

    sum=0
    for val in values:
        sum += val

    return sum+num

print(calc(100))
print(calc(100, 200))
print(calc(100, 200, 300, 400, 500))
print()

# 4) 키워드 가변 인수 - 여러개(n개) 전달시 key와 value 전달
# Ex1)
def sub(**su):
    print(type(su))
    for val in su.values():
        print(val)

sub(a=1, b=2, c=3)
sub(fru="사과", veg="당근")
print()

# Ex2) 웹 호출 서버, 포트, 경로명, id="홍길동"&pwd="123" 키워드 가변인수로 전달 params

def urlPath(server, port, program, **params):
    url="http://" + server +  ":" + port + program + "?"

    for key, values in params.items():
        url += key + "=" + values + "&"

    return url

print(urlPath("www.goole.co.kr", "80", "/search", id="abc123", pwd="xyz123"))
print()

# Ex3) 혼합 사용 일반(위치)인수, 키워드인수, 기본값 인수, 가변 인수, 키워드 가변 인수 순서 
def fun(su, cnt=2, *values, **member):
    print(su, cnt, values, member)

fun(1)                            # 1, 2, (), {}
fun(11, 12, 13)               # 11, 12, (13, ) { }
fun(2, 3, 11, 23, 13)       # 2, 3, (11, 23, 13, )  { }
fun(88, 99, id="abc", pwd="1234")    # 88 99 () { id="abc", pwd="1234")}

