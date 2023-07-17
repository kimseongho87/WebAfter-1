# Swap : 두수 값을 서로 교환
a=10
b=20
print(a, b)

a, b=b, a
print(a, b)

my_list=[3, 5]
my_list[0], my_list[1]=my_list[1], my_list[0]
print(my_list[0], my_list[1])


# 버블정렬 O(n^2) loop를 돌면서 인접한 데이터간의 swap 연산으로 정렬
array=[188, 162, 120, 50, 150, 177, 105]
idx=len(array)

for end in range(idx-1, 0, -1):              # 6            5       4       3      2     1+
    for cur in range(0, end):                  #  0~6     0~5    0~4     0~3    0~2 0~1
       if array[cur] > array[cur+1]:          # [0] 188 > [1] 162     / [1] 188 > [2] 120   / [2] 188 > [3] 50   / [3] 188 >  150 [4]
           array[cur], array[cur+1]=array[cur+1], array[cur]    # [0] 162  [1] 188    / [1] 120 [2] 188
           print(array) 

print("최종", array)                                     