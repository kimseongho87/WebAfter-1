# 중복값 처리
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot=arr[len(arr)//2]
    left, mid, right=[], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)

        print(left, mid, right)
    
    return quick_sort(left) + mid + quick_sort(right)


if __name__=="__main__":
    arr = [5, 7, 9, 0, 3, 1, 1, 6, 2, 4, 8]
    print(quick_sort(arr))