# 순서형 index : str, list, stack
#  삽입, 삭제, 검색, 수정 

# stack : LIFO / Last in First Out / list를 활용해서 원소 삽입, 추출

stack=[]
stack.append(10)         # push
stack.append(20)
stack.append(30)
stack.append(40)
print("길이:", len(stack))

print(stack.pop())            # 출력하면서 제거
print("길이:", len(stack))

while stack:
    print(stack.pop())

print("길이:", len(stack))
print()

stack.append(77)            # push
stack.append(88)
print("길이:", len(stack))

while stack:
    print(stack.pop())
print("길이:", len(stack))
print("\n\n")

# stack 자료구조를 이용해서 주어진 문자열 거꾸로 출력 
def reverse_string(string):
    stack=[]
    result=""

    for char in string:         # 문자열을 스택에 한 글자씩 추가
        stack.append(char)

    while stack:
        result +=stack.pop()

    return result

print(reverse_string("Hello, World"))




