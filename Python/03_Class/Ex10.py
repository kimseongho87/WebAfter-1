# 함수, 생성자 - 상속시 데이터 전달
class Animal:
    def walk(self):
         print("걷는다")

class Dog(Animal):
    def __init__(self, name):
        self.name=name

    def eat(self):
        print(self.name, ":사료 먹습니다.")


if __name__ == "__main__":
    d=Dog("멍멍이")
    d.walk()
    d.eat()