# Ex1)
def mul(myList):
    result=myList[5]*myList[6]
    myList.append(result)
    print(myList)

myList=["2021-01-02", "나나문구 홍익점", "직영대리점", "기타", "포스트잇노트", 70, 1700]
mul(myList)

# Ex2) Class : 변수와 함수 집합
def hap(su, value):
    print(su+value)

hap(10, 20)
hap(30, 40)
hap(50, 60)
print("\n\n")

print("클래스")
class Calc:                                    # 클래스 = 함수 + 변수
    def input(self, su, value):         # 함수(매개변수....)
        self.su=su                            # self.su 변수
        self.value=value
        self.hap=0

    def output(self):                      # 함수
         print(self.su)
         print(self.value)
         print(self.su + self.value , "\n")

if __name__ == "__main__":          #  생략가능
      c=Calc()                                 #   객체
      c.input(10, 20)
      c.output()

      a=Calc()
      a.input(11, 21)
      a.output()

      b=Calc()
      b.input(22, 23)
      b.output()



