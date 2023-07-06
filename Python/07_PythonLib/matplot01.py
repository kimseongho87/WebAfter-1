import matplotlib.pyplot as plt
import numpy as np

# Ex1) 직선 그래프 plot() - X, Y
x=[1, 2, 3]
y=[1, 2, 3]

plt.title("My Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y)
# plt.show()
# plt.savefig("picture.png")

# Ex2) 직선 그래프 - 옵션
x=np.arange(-9, 10)    # 곡선
y=x**2
plt.title("My Plot")
plt.xlabel("X")
plt.ylabel("Y")

# 옵션
plt.grid()
plt.plot(x, y, linestyle=":", marker="o", markersize=8, markerfacecolor="yellow", markeredgecolor="blue")
# plt.show()

# Ex3) 직선, 곡선
x=np.arange(-9, 10)    # 곡선
y=x**2
z=-x

plt.title("My Plot")
plt.plot(x, y, linestyle="-", marker="*",  color="red", label="y=x*x")
plt.plot(x, z, linestyle=":", marker="o", color="blue", label="z=-x")
plt.legend(loc="upper right")
# plt.show()

# Ex4) 두개 직선 그래프 
x=np.linspace(0, np.pi*10, 500)    # 0~pi*10 500개 균일 값
f, a=plt.subplots(2, 1)
a[0].plot(x, np.sin(x))
a[1].plot(x, np.cos(x))
plt.show()

