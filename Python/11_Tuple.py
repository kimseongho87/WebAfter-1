# 튜플 활용
# packing : 하나의 변수에 여러개의 값을 넣는것
su=(1, 2, 3)
print(su, type(su))

#upacking : 패킹된 변수에 여러개의 값을 꺼내 오는것
one, two, three=su
print(one, type(one))
print(two, type(two))
print(three, type(three))
print()

city, latitude, longitude=('Seoul', 37.541, 126.986)
print(city, type(city))
print(latitude, type(latitude))
print(longitude, type(longitude))
print()

# 알고리즘 두개변수의 값을 교환
x=5
y=10
print(x, y)     # 5 10

imsi=x          #  5
x=y               #  10
y=imsi          #  5
print(x, y)   

a=66
b=77
print(a, b)

a, b=b, a
print(a, b)

# a=[], b=(), c={}
