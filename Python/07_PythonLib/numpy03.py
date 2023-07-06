import numpy as np

# 파일 가져오기
path="C:\\Users\\JMH\Desktop\\teacher\\workspace\\Python\\07_PythonLib\\ratings.dat"

data=np.loadtxt(path, delimiter="::", dtype=np.int64)    # np.genfromtxt()
print(data.shape)    # (1000209, 4)

# 사용자 id 1,   영화 id 1193,  평점  5 978300760]
print(data[:5, :])      # print(data[0:5, 0:4])   [행 start:end:stpe, 열 start:end:step]

# 전체 평점 평균 계산하기
print(np.mean(data[:, 2]))

# 사용자별 평점 평균
user_id=np.unique(data[:, 0])
print(user_id.shape)

mean_value=[]     # 리스트
for id in user_id:
    # data_user=data[data[:, 0] == id]
    
    data_user=data[np.where(data[:, 0] == id)]       # if data[:, 0] == id : 
    value=data_user[:, 2].mean()
    mean_value.append([id, value])    # list

print(mean_value[:10])

# 최고 평점
arr_mean_values=np.array(mean_value)
print(np.max(arr_mean_values[:, 1]))

# 사용자별 평균평점 저장
np.savetxt("C:\\Users\\JMH\Desktop\\teacher\\workspace\\Python\\07_PythonLib\\id_ratings.csv", 
                  arr_mean_values, delimiter=',' , fmt="%.1f")

