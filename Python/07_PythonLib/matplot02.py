import matplotlib.pyplot as plt
import numpy as np

# Ex5) 막대 그래프 bar()
# x=np.arange(-9, 10)
# plt.title("My Bar")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.bar(x, x**2)
# plt.show()

# Ex6) 스캐터 그래프 scatter()
x=np.random.rand(10)
y=np.random.rand(10)

color=np.random.randint(0, 100, 10)     # RGB(0, 256, 12)
sizes=np.pi * 1000 * np.random.rand(10)

plt.scatter(x, y, c=color, s=sizes, alpha=0.7)
plt.show()