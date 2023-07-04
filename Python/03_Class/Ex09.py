# 함수, 생성자 - 상속시 데이터 전달
class Animal:
    def setName(self, name):
        self.name=name

    def walk(self):
         print("걷는다")


class Dog(Animal):
    def eat(self):
        print(self.name, ":사료 먹습니다.")


if __name__ == "__main__":
    d=Dog()
    d.setName("멍둥이")
    d.walk()
    d.eat()