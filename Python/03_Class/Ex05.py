class Su:                                         # 클래스
    def __init__(self, num, value):     # 생성자
        self.num=num                       #  self변수(속성), 매개변수(지역변수)
        self.value=value

    def disp(self):                               # 함수(기능)
        print("%d %d"%(self.num, self.value))


if __name__ == "__main__":
    s=Su(10, 20)                # 데이터를 클래스 전달해야된다.  데이터를 전달하는 방법은 생성자 또는 함수
    s.disp()

    a=Su(77, 88)
    a.disp()