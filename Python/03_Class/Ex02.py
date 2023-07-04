class Sungjuk:      # self=pengsoo, self=hong
    def inputData(self, name, kor, eng, mat):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat
      #   self.tot=0
      #   self.avg=0

        """
         pengsoo.name=펭수
         pengsoo.kor=70
         pengsoo.eng=80
         pengsoo.mat=90
         pengsoo.tot=0
         pengsoo.avg=0
        """
    def total(self):
        self.tot=self.kor+self.eng+self.mat

    def average(self):
        self.avg=self.tot / 3

    def disp(self):
        print("%s %d %0.2f"%(self.name, self.tot, self.avg))
        
if __name__ == "__main__":
    pengsoo=Sungjuk()
    pengsoo.inputData("펭수", 70, 80, 90)
    pengsoo.total()
    pengsoo.average()
    pengsoo.disp()

    hong=Sungjuk()
    hong.inputData("홍길동", 90, 90, 80)
    hong.total()
    hong.average()
    hong.disp()