array= [6, 5, 3, 1, 8,  7, 2, 4 ]
idx=len(array)

for end in range(1, idx):                 # 4 5 6 7
     for cur in range(end, 0, -1):      #  4321
           if array[cur-1] > array[cur]:      # array[]  >  array[]
                  array[cur-1], array[cur]=array[cur], array[cur-1]    
           #print(array) 
            #  [1, 3, 5, 6, 8,  7, 2, 4 ]
print(array)


# 10분 시작합니다.