import numpy as np

# Ex1) list를 사용하여 numpy 배열 생성할수 있다.
my_list=[10, 22, 34, 40, 15]
my_array=np.array(my_list)     # 동일한 자료형, 문자열 넣으면 모든 원소가 문자열로 바꿈
print(my_array)
print("배열의 크기:", my_array.size)
print("배열의 차원:", my_array.shape)
print("배열의 원소타입:", my_array.dtype)
print()

copy_value=my_list.copy()
copy_value.sort()
print("정렬:", copy_value)
print("원본:", my_array)
print()

# ([[]])
array=np.array([[11, 20, 3, 4, 5], 
                        [4, 5, 6, 70, 8]])
print(array)
print(array.size)
print(array.shape)
print(array.dtype)

array.sort(axis=0)
print("열기준 정렬\n", array)