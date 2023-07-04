class Calculation:
    def setData(self, su, buho, value):      # self=c, su, buho, value
        self.su=su
        self.buho=buho
        self.value=value
        # self.yonsan=0

    def result(self):
      if self.buho == "+":
          self.yonsan=self.su + self.value
      elif self.buho == "-":
          self.yonsan=self.su - self.value
      elif self.buho == "*":
          self.yonsan=self.su * self.value
      elif self.buho == "/":
          self.yonsan=self.su // self.value
    
    def disp(self):
        print("%d %s %d = %d"%(self.su, self.buho, self.value, self.yonsan))


if __name__ == "__main__":
    su=int(input("수 입력:"))
    buho=input("부호 입력:")
    value=int(input("수 입력:"))

    c=Calculation()
    c.setData(su, buho, value)
    c.result()
    c.disp()