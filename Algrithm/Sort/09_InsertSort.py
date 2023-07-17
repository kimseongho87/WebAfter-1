def find_insert(array, data):       # [], 55 / 33 77 88, 55  / 33  55  77  88, 100
    idx=-1                                   # 삽입할 위치가 없는 위치를 -1로 지정
    for i in range(0, len(array)):
        if array[i] > data:                # 33  55  77  88  > 100
            idx=i                                # 1
            break
        
    if idx == -1:                             # 삽입할 위치를 찾지 못함
        return len(array)                  # 0
    else:
        return idx                             # 1
   
array=[]
inspos=find_insert(array, 55)
print(inspos)

array=[33, 77, 88]
inspos=find_insert(array, 55)
print("삽입할 위치", inspos)       # 1

array=[33, 55, 77, 88]
inspos=find_insert(array, 100)    # 4
print("삽입할 위치", inspos)