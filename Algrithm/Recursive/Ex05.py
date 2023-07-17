# 팩토리얼 구하기
val=1
for n in range(10, 0, -1):
    val * n
print(val)
print()

def factorial(num):   # 5
    if num <=1:
        return 1
    return num * factorial(num-1)   # 5 4 / 4 3 / 3 2 / 2 1

if __name__ == "__main__":
    print(factorial(10))