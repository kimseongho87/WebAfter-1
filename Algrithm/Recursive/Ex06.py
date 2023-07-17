# N 제곱
tab=' '
def pow(x, n):
    global tab
    tab +=' '
    
    if n==0:
        return 1
    
    print(tab +"%d * %d ^ (%d-%d)"%(x, x, n, 1))
    return x * pow(x, n-1)

print(pow(2, 4))
print()

# 배열의 합
def arr_sum(arr, n):
    if n <=0:
        return arr[0]
    return arr[n] + arr_sum(arr, n-1)     # 5, [5, 3, 7, 2, 1] 4 /  4, [5, 3, 7, 2, 1] 3/  3, [5, 3, 7, 2, 1] 2 /  2, [5, 3, 7, 2, 1] 1 /  1 

if __name__ == "__main__":
    array=[5, 3, 7, 2, 1]
    print(arr_sum(array, len(array)-1)) 