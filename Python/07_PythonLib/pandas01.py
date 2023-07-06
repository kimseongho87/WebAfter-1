import pandas as pd

# Series(시리즈) : 1차원배열  List, Dic
# Ex1) List
my_list=[10, 20, 30, 40]
su=pd.Series(my_list)
print(su)
print(su.index)
print(su.values)
print(su.sum())
print(su.mean())
print()

# Ex2) index 지정
arr=pd.Series(['분식이', "쏘니", "홍길동", "변사또"],
                       index=["하나", "둘", "셋", "넷"],
                       name="출석부")
print(arr)
print()

#Ex3) Dict
dic=pd.Series({'name':'김분식', 'age':30, "gender":"male", "job":"분석가"})
print(dic)
print()

# 2. DataFrame 
df=pd.DataFrame([[1000, '과자', '2021-12-31', '반품'],
                              [2000, '음료', '2022-2-3', '정상'], 
                              [3000, '아이스크림', '2022-5-5', '정상'], 
                              [1000, '과자', '2021-12-31', '반품']],
                              columns=['가격', '종류', '판매일자', '반품여부'])
print(df)
print()

# Ex3) 컬럼 출력
print(df['가격'])
print(df['종류'])

print(df['가격'].sum())
print(df['가격'].mean())
print()

# Ex3) 원하는 컬럼과 행 추출
price=df[['가격', '종류', '판매일자']]
print(price)
print()

data=df.loc[0:2, '가격':'판매일자']
print(data)
