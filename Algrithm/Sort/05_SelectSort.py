array=[4, 6, 1, 3, 5, 2]
idx=len(array)   # 6

 # [1, 2, 4, 3, 5, 6]        2 3 4 5
for i in range(0, idx):     # 2
    min_idx=i                  # 2
    for j in range(i+1, idx):    # 345
         if array[min_idx] > array[j]:   # array[3]  3  > 6    array[5]
            min_idx=j     #  array[3] 3
        
    array[i], array[min_idx]=array[min_idx], array[i]
   # array[2] 3,, array[3] 4  = array[3] 3 , array[2]   4

   # [1, 2, 3, 4, 5, 6]
    print(array)

print("최종", array)


# 5분 시작

