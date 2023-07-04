class Human:               # 클래스
    def __init__(self, name, weigth):    # 생성자   self  hong, name 홍길동, weigth 75.5
        self.name=name
        self.weigth=weigth

    def eat(self):                                    # 함수
        self.weigth += 0.1

    def walk(self):
        self.weigth -= 0.1

    def disp(self):
        print("%s  님 현재 %0.2f kg 되었습니다."%(self.name, self.weigth))

    def __str__(self):
         return "%s 님 현재 %0.2f kg 되었습니다."%(self.name, self.weigth)

if __name__ == "__main__":
    hong=Human("홍길동", 75.5)
    hong.eat()
    hong.eat()
    hong.eat()
    hong.walk()
    hong.disp()

    print(hong)     # 원래는 객체 출력 할당 주소값출력... str의 리턴 값이 출력된다.


