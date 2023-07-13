"""
   알고리즘 : 자료구조 + 알고리즘

   자료구조 : 배열(list), 스택, 큐, 그래프, 트리 
   알고리즘 : 탐색, 정렬......
   
   탐색 : 선형탐색, 이진탐색, 깊이우선탐색(DFS) 그래프/스택, 너비우선탐색(BFS)
"""

arr=[3, 8, 2., 7, 6, 10, 9]
print(arr[0], arr[3], arr[-1])
print(arr.index(8))  
print()

def my_index(su, target):
    result=[]

    for i in range(len(su)):
        if su[i] == target:
            result.append(i)
        
    if len(result) == 0:
        return -1
    else:
      return result
    
su=[3, 8, 2, 7, 6, 7, 10, 9]
print(my_index(su, 7))
