# 내장함수 :  점 . 연산 (클래스, 모듈), print(), input() 명 사용

print("절대값:", abs(1))
print("절대값:", abs(-3.5))
print("아스키 코드:", chr(97), chr(65))
print()

print(dir(list))
print(dir([1, 2, 3, 4, 5]))
print(dir(dict))
print(dir({'1':'a'}))
print()

print(5//2)
print(5%2)
print("몫과 나머지", divmod(5, 2))
# a, b=5//2, 5%2


# enumerate 인덱스 값을 포함 데이터를 반환
arr=[10, 20, 30, 40, 50]

for val in arr:
    print(val, end=" ")
print()

for idx, val in  enumerate(arr):
    print(idx, val)
print()    

# 5시 시작합니다.
