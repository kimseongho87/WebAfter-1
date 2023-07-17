def quick_sort(arr):
    if len(arr) <=1:
      return arr
    
    pivot=arr[len(arr)//2]     # idx 4 : 105
    # print(pivot)
    left, right=[], []

    for num in arr:
       if num < pivot:
          left.append(num)
       elif num > pivot:
          right.append(num)

    print(left, pivot, right)
    # [50] 105 [188, 150, 168, 162, 120, 177]

    return quick_sort(left)+[pivot]+quick_sort(right)

if __name__=="__main__":
    arr = [188, 150, 168, 162, 105, 120, 177, 50]
    print(quick_sort(arr))       