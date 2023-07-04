# 부모 클래스 생성자 상속

class Animal:
    def __init__(self, name, age):   # 초쿄", 3,
       self.name=name
       self.age=age

    def getAnimal(self):
        print("%s %d"%(self.name, self.age))

    def speak(self):
        print("안녕하세요")  
    

class Cat(Animal):
    def __init__(self, name, age, bread):    # 초쿄", 3, " 페르시안"
        super().__init__(name, age)             # 생성자 상속
        self.bread=bread

    def disp(self):
        print("%s 야옹"%(self.bread))

if __name__ == "__main__":
    cat=Cat("초쿄", 3, " 페르시안")
    cat.getAnimal()
    cat.speak()
    cat.disp()


"""
    기본자료형 : int, float, bool
    순서자료형 : str, list, tuple
    비순서자료형 : set, dic
    사용자정의 자료형 : class (변수,함수),  self, 생성자, 상속 / 객체, .(점)
"""