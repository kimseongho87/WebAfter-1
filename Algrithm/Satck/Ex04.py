# 실습문제 - 햄버거 1231

def solution(data):
    answer=0
    stack=[]

    for i in data:
        stack.append(i)   # 2
        # print(stack)
        # print(stack[-4:])

        if stack[-4:] == [1, 2, 3, 1]:           #  [1, 2, 3, 1]==[1, 2, 3, 1] [-4:-1]
            answer +=1
            for i in range(4):
                stack.pop()

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))