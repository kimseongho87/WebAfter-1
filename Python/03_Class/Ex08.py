# 상속 : 클래스가 다른 클래스 상속 받는다.

class Animal:
   def walk(self):
      print("걷는다")
   
   def eat(self):
      print("먹는다")


class Human(Animal):      # walk(), eat()
   def wave(self):
      print("손을 흔든다")


class Dog(Animal):            # walk(), eat()
   def wave(self):
      print("꼬리를 흔든다")
      
if __name__ == "__main__":
   a=Animal()
   a.walk()
   a.eat()
   print()

   h=Human()
   h.walk()
   h.eat()
   h.wave()
   print()

   d=Dog()
   d.walk()
   d.eat()
   d.wave()
