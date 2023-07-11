def my_append(num, su):    # 맨마지막 추가
    num[-1]=su
    return num

def my_insert():         # 중간에 추가
    pass    # 지금 안됨~~~

def my_index(num, su):             # 해당데이터의 위치(번지)
    for i in range(len(num)):
        if su==num[i]:
            return i
    return -1

def my_remove():
    pass   # 지금 안됨

if __name__ == "__main__":
    num=[10, 11, 12, 13, 14]
    print(my_append(num, 77))
    print(my_index(num, 12))


   

