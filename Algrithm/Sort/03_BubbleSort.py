N=int(input())        # 3
A=list(map(int, input().split()))   # 3 2 1


count=0
for end in range(N-1, 0, -1):        # 3           2        1
    for cur in range(0, end):           # 012      01       0
        if A[cur] > A[cur+1]:             # [0] 2 > 1 [1]  / [1] 3 > 1 [2]
            A[cur], A[cur+1]=A[cur+1], A[cur]
            count +=1
            # print(A)
   
print(count)

# 1시 시작

