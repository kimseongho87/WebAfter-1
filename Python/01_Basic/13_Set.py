# 자료구조 : [ ], ( ), { }
#  [ ] 대괄호: index 0~~, 데이터 중복 가능, 추가/수정/삭제
#  ( ) 소괄호: index 0~~, 데이터 중복 가능, list 읽기 전용(추,수,삭 불가), packing, unpacking

#  {k:v} 중괄호  : key, value 구성, 키는 중복 불가, 추가/수정/삭제
#  { }, set(자료구조) : 중복값을 허용 안함, 순서유지 안됨, 추가/삭제

a=set(["apple", "banana", "melon"])      # 리스트를 입력하여 사용
print(a, type(a))

b=set(("월요일", "화요일", "금요일"))    # 튜플을 입력하여 사용
print(b, type(b))

c=set("Hello")                                          #  문자을 입력하여 사용
print(c, type(c))     
print("\n\n")

d={"오늘은", "습해요", "금요일", "금요일"}
print(d)

d.add("F")
print(d)

d.remove("F")
print(d)

print(d.pop())
print(d)

a.update(b)              # 집합끼리 결합   {'apple', 'banana', '월요일', 'melon', '금요일', '화요일'}
print(a)


