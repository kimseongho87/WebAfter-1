import numpy as np

# Ex2)  다양한 배열 초기화 방법  10분 시작
print(np.arange(4))
print(np.arange(1, 10, 2))
print()

print(np.zeros((4, 4), dtype=float))
print(np.ones((3, 3), dtype=str))
print(np.full((2, 3), 5))
print(np.eye(3))     # 3*3
print()

print(np.random.random(5))
print(np.random.randint(0, 10, size=(3, 3)))
print(np.linspace(0, 1, 5))