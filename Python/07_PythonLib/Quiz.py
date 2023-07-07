import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path="C:\\Users\\JMH\\Desktop\\teacher\\workspace\\Python\\06_WebCrawler\\movie.xlsx"
data=pd.read_excel(path)
print(data.info())
print(data.head(10))

# 복사
movie=data.copy()
print(data.head())

# 이상치/결측치 처리방법 - 처리 삭제, 0.0, 평균값 대체
# 이상치 - np.nan 
movie['Greade']=movie['Greade'].replace("보고싶어요", np.nan)
movie['Greade']=movie['Greade'].replace("보는중", np.nan)
print(movie.head())

# object - float      a=10, a += 5
movie['Greade']=movie['Greade'].astype(float)

# 평균값
mean_value=movie['Greade'].mean()
print(mean_value)
movie['Greade']=movie['Greade'].fillna(round(mean_value, 1))
print(movie.head())

# 기술통계량
print(movie.describe())

# 그래프 그리기
ratings=movie['Greade']
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.hist(ratings, bins=5, edgecolor="black")    # 빈도수 5개, 구간 테투리 검정색
plt.show()