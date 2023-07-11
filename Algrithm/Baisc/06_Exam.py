# 클래스로 작성
class MyList:
   def __init__(self, data):      
        self.data=data

   def my_sum(self):
      hap=0
      for i in range(len(self.data)):
         hap=hap+self.data[i]
      return hap
   
   def my_max(self):
    max=self.data[0]                     # 11
    for i in range(len(self.data)):
        if max < self.data[i]:            # 12 < 14
            max=self.data[i]              # 12
    return max

   def my_min(self):
      min=self.data[0]
      for i in range(len(self.data)):
         if min > self.data[i]:
               min=self.data[i]    
      return min

   def my_len(self):
      count=0
      for i in self.data:
         count +=1
      return count

if __name__ == "__main__":
      my_list = MyList([55, 88, 99, 1, 6, 7])
      print("Sum:", my_list.my_sum())
      print("Length:", my_list.my_len())
      print("Max:", my_list.my_max())
      print("Min:", my_list.my_min())


      # 12분 시작