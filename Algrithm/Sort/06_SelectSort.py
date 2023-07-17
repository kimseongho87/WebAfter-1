

def sorting_validation(arr, N, B):
    for i in range(0, N):
      min_idx=i
      for j in range(i+1, N):
         if arr[min_idx] > arr[j]:
            min_idx=j

      arr[i], arr[min_idx] = arr[min_idx], arr[i]
      # print(arr)

      if arr==B:
         return 1
      return 0

N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
print(sorting_validation(A, N, B))