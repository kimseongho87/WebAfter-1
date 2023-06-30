# 집합연산
# 합집합 : 두 집합의 모든 원소 반환
x={1, 2, 4, 7}
y={2, 3, 7, 9}
print(x | y)                          # {1, 2, 3, 4, 7, 9}
print(x.union(y))
print(y.union(x), "\n")

# 교집합 : 두 집합이 공통적으로 포함한 원소 반환
print(x & y)                           # {2, 7} 
print(x.intersection(y))
print(y.intersection(x), "\n") 

# 차집합 : 인자의 집합 원소 제거한 원소 반환
print(x-y)          #  1, 4
print(x.difference(y))

print(y-x)          #  3, 9
print(y.difference(x), "\n")

# 배타적 차집합 : 한쪽 집합에만 있는 원소 반환
"""
   x={1, 2, 4, 7}
   y={2, 3, 7, 9} 
"""
print(x ^ y)                                     # {1, 3, 4, 9}
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))

# 부분집합 확인 (s집합은  p집합에 부분집합이다. ) : 일부 포함
p={"A", "B", "C", "D", "E"}
s={"B", "C", "D"}
print(s <= p)              # T
print(s.issubset(p))
print(p.issubset(s), "\n")

# 상위집합 확인 (p집합은 s집합의 상위집합이다.)  : 모두 포함
print(s >= p)                # F
print(s.issuperset(p))    # F
print(p.issuperset(s))    # T