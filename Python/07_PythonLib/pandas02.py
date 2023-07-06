import pandas as pd

path="C:\\Users\\JMH\\Desktop\\teacher\\workspace\\Python\\07_PythonLib\\drinks.csv"
data=pd.read_csv(path)

# Ex1) 데이터 확인
print(data.info())
print(data.head())
print()

# Ex2) 기술 통계량 : 총갯수, 열의 평균값, 데이터의 분산, 열의 큰값/작은값 25% 50% 75%
print(data.describe())
print()

# Ex3) 상관관계 : -1~1 
corr=data[['beer_servings', 'wine_servings']].corr(method='pearson')
print(corr)
print()

# Ex4) 결측치 : 삭제, 대체 값 (0, '~~') / 평균값
# data_null=data['continent'].isnull()
# print(data_null.sum())
print(data['continent'].isnull().sum())

data['continent']=data['continent'].fillna("OT")
print(data.head(10))
print()

# 전체 평균보다 많은 알코올을 섭취하는 대륙
# 평균 알코올 섭취
total_mean=data.total_litres_of_pure_alcohol.mean()
print("평균 알코올 섭취율:", total_mean)    # 4.7

# 그룹별로 평균
continent_group=data.groupby('continent')
continent_mean=continent_group['total_litres_of_pure_alcohol'].mean()
print("그룹별 알코올 섭취율:", continent_mean)

# 결론
continent_over_mean=continent_mean[continent_mean >= total_mean]
print("결론:", continent_over_mean)
print()

# 평균 맥주 소비가 가장 높은 대륙
beer_continent=continent_group['beer_servings'].mean()
print(beer_continent)
print("대륙:", beer_continent.max(), beer_continent.idxmax())
print()

wine_continent=continent_group['wine_servings'].mean()
print(wine_continent)
print("대륙:", wine_continent.max(), wine_continent.idxmax())

import matplotlib.pyplot as plt
# 그래프 - 대륙별
lables=data['continent'].value_counts().index.tolist()
value=data['continent'].value_counts().values.tolist()
explode=(0, 0, 0, 0.50, 0, 0)

plt.pie(value, labels=lables, explode=explode, autopct="%.1f%%")
plt.show()

# 12분 시작

