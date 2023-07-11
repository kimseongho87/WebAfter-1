su=[11, 12, 14, 55, 77, 99, 1, 2]  # 자료구조(자료형)
print(sum(su))
print(max(su))
print(min(su))
print(len(su))
print()

# 가장 큰값
# 가장 작은값
# 길이 count
# 합

# 자료구조 데이터 추가, 삭제, 검색
num=[10, 11, 12, 13, 14]

# 추가
num.append(77)
num.insert(3, 88)
print(num)

# 검색
print(num.index(10))    # 해당 데이터의 index
print(num[3])               #  해당 index의 데이터  


# 삭제
num.remove(11)          # 해당 데이터를 삭제
del(num[3])                  # 해당 번지를 삭제
print(num)

# 수정
num[0]=88
print(num)