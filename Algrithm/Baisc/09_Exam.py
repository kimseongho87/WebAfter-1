
def my_len(data):
   count=0
   while data:
      data.pop()
      count=count+1
   return count  

def my_sum(data):   
   hap=0
   while data:
      hap=hap+data.pop()    #  hap += data.pop()
   return hap

def my_max(data):      
      max_value=data.pop()
      while data:
          item=data.pop()
          if item > max_value:
              max_value=item
      return max_value

def my_min(data):   
      pass

if __name__ == "__main__":
   stack=[]
   stack.append(10)
   stack.append(7)
   stack.append(160)
   stack.append(1)
   stack.append(70)

   # print(my_len(stack))
   # print(my_sum(stack))
   print(my_max(stack))   


