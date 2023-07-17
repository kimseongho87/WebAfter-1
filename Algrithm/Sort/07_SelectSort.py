array= [7, 5, 11, 6, 9, 8000, 10, 6, 15, 12]
idx=len(array)

for i in range(0, idx):
    min_idx=i                                          
    for j in range(i+1, idx):                       
            if array[min_idx] > array[j]:         
                min_idx=j         
    
    array[i], array[min_idx] = array[min_idx], array[i]   

print("결과:", array)    
print("중앙값", array[idx//2]) 