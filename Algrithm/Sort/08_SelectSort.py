array=[[55, 32, 250, 44], 
            [88, 1, 67, 23]]

result=[]
for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        result.append(array[i][j])
print(result)

idx=len(result)
for i in range(0, idx):
    min_idx=i                                          
    for j in range(i+1, idx):                       
            if result[min_idx] > result[j]:         
                min_idx=j         
    result[i], result[min_idx] = result[min_idx], result[i]   
    
print("정렬:", result)
print("중앙값:", result[idx//2])
        