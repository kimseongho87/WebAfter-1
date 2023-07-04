class Car:
    def __init__(self, color, wheelSize, displacement):
        self.color=color
        self.wheelSize=wheelSize
        self.displacement=displacement

    def forward(self):
        print("%s %d %d의 자동차가 전진합니다."%(self.color, self.wheelSize, self.displacement))

    def backward(self):
         print("%s %d %d의 자동차가 후진합니다." %(self.color, self.wheelSize, self.displacement))

    def trunLeft(self):
        print("%s %d %d의 자동차가 좌회전합니다." %(self.color, self.wheelSize, self.displacement))

    def trunRight(self):
        print("%s %d %d의 자동차가 우회전합니다." %(self.color, self.wheelSize, self.displacement))   

if __name__ == "__main__":
    sonata=Car("RED", 16, 2000)
    sonata.forward()
    sonata.backward()
    sonata.trunLeft()
    sonata.trunRight()

    # 상속, 추상클래스, 함수재정의, 중복