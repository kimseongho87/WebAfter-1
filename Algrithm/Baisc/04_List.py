
# PPT 1번) 리스트의 합
def soultion(x):
    answer=x[0] + x[-1]          # int(x[0]) + int(x[-1])
    return answer

print(soultion([5, 3, 8, 2]))     # 키보드 입력
print()


# 2번) 정렬된 리스트에 원소 삽입
def soultion(L, x):
    L.append(x)
    L.sort()
    answer=L
    return answer

print(soultion([20, 37, 58, 72, 91], 65))
print()


# 3번) 배열 원소의 길이
def solution(strlist):
    answer=[]

    for s in strlist:
        answer.append(len(s))

    return answer
       
print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))
print()

# 4번) 배열 뒤집기
def solution(num_list):
    answer=[]
    num_list.reverse()
    answer=num_list
    return  answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))
print()

# 5번) 제일 작은 수 제거
def solution(arr):
    answer=[]

    if len(arr)==0 or len(arr)==1:
        answer.append(-1)
    else:
        arr.remove(min(arr))
        answer=arr

    return answer

print(solution([4, 3, 2, 1]))
print(solution([10]))
print()

# 6번)
def solution(L, x):
    answer=[]

    for i in range(len(L)):   # (0, len, 1)
        if x==L[i]:
            answer.append(i)

    if x not in L:
      answer.append(-1)

    return answer

print(solution([64, 72, 83, 72, 54],  72))        
print(solution([64, 72, 83, 72, 54],  83))     
print(solution([64, 72, 83, 72, 54],  49))     
            

