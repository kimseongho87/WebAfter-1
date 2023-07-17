# 최소값
array=[55, 88, 33, 77]
min=array[0]   # 55
for i in range(1, len(array)):
    if min > array[i]:    # 33 > 77
      min=array[i]       # 33
print(min)

# idx 활용 
array=[55, 88, 33, 77]
min_idx=0
for i in range(1, len(array)):
   if array[min_idx] > array[i]:   # array[2]  33 > 77 array[3]
      min_idx=i

print(array[min_idx])
