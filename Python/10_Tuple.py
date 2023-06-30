# Tuple - 읽기 전용 List
a=(1, 2, 'a', 'b')
print(a, type(a))

b=(1)         
print(b, type(b))            #  int

c=1, 2, 3, 4                    # 괄호 생략가능
print(c, type(c))

# indexing & slicing
print(c[0])
print(c[1:3])

# 튜플 연산
d=(3, 4)
e=(5, 6)
print(d+e)
print(d*3)
print()

# 튜플함수, 내장함수, in/not 연산자
t=(10, 20, 30, 40, 10, 50, 60)
print(t.index(50))
print(t.count(10))

print(len(t))
print(max(t), min(t))
print(sorted(t))
print(sorted(t, reverse=True))
