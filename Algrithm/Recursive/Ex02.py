# 재귀 함수 호출 동작

def open_box():
    global count       # 3 2 1

    print("종이 상자를 엽니다.")

    count -= 1        # 2 1  0

    if count == 0:
        print("** 반지를 넣고 반환합니다.")
        return 
    
    open_box()

    print("종이 상자를 닫습니다")

if __name__=="__main__":
    count=3
    open_box()

