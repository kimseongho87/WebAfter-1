class Apple:      # 생성자, 소멸자 - 기본값
    def __init__(self):
        print("생성자 >>>>>>")

    def disp(self):
        print("dips 함수 >>>>>>")

    def __del__(self):
        print("소멸자 >>>>>>")


if __name__ == "__main__":
    a=Apple()                # 생성자 
    a.disp()                     # disp()

    b=Apple()                # 생성자
    b.disp()                    # disp()

                                    # a 소멸자,  b 소멸자