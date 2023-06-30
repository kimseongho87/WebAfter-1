# Dictionary : key, value 구성 탐색 속도가 빠르다. / 실무에서 가장 많은 사용하는 자료구조
dic={"name":"홍길동", "phone":"010-123-1234", "birth":"2004-12-25"}
print(dic, type(dic))
print(dic["name"])
print(dic["phone"])
print(dic["birth"])
print("\n\n")

# 다양한 key 설정
sukey={1:"홍길동", "2":"010-123-1234", 33.3:"2004-12-25"}
print(sukey, type(sukey))
print(sukey[1])
print(sukey["2"])
print(sukey[33.3])
print("\n\n")

# 서로 다른 자료형의 key, value
nary={"name" : "펭수",  3:[1, 2, 3], 24.5:"B"}
arr=nary[3]
print(arr, arr[0], arr[1], arr[2])
print("\n")

#  추가, 삭제, 수정
#  dic={"name":"홍길동", "phone":"010-123-1234", "birth":"2004-12-25"}

dic["addr"]="서울시 강남구 역삼동"
print(dic)

dic["phone"]="666-7777-8888"
print(dic)

del dic["addr"]
print(dic)
print("=======================\n\n")

#  dic={"name":"홍길동", "phone":"010-123-1234", "birth":"2004-12-25"}
print(dic.get("name"))
print(dic.keys())          # key 전체 출력
print(dic.values())       # value  전체 출력
print(dic.items())         # key, value 전체 출력
print(type(dic.keys()))
print(type(dic.values()))
print(type(dic.items()))

key=list(dic.keys())
print(key, type(key), key[0])

value=list(dic.values())
print(value, type(value), value[1])

item=list(dic.items())   # [('name', '홍길동'), ('phone', '666-7777-8888'), ('birth', '2004-12-25')]
t=tuple(item[0])          #  ('name', '홍길동')
print(t[0], t[1])

dic.clear()                       # 전체삭제
print(dic)
print("\n")


# 두개 병합
a={"name" : "펭수",  "key":210}
b={"job" : "EBS 연습생"}
a.update(b)
print(a)

# in / not in
print("name" in a)
print("key" not in a)



