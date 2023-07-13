def find_max(arr):              # 최대값 함수
    max_val=arr[0]

    for val in arr:
        if val > max_val:
            max_val=val

    return max_val

def find_min(arr):              # 최소값 함수
    min_val=arr[0]

    for val in arr:
        if val < min_val:
            min_val=val

    return min_val

arr=[55, 88, 102, 77, 88, 1, 6]
arr_max=find_max(arr)          
arr_min=find_min(arr)            
print(arr_max-arr_min)           

# 10분 시작합니다.