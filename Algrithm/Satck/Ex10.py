from StackFixed import Stack

def  is_palindrome(string):    # level
   end=len(string) // 2
   # print(end)

   stack=Stack(end)
   for char in string[:end]:   
        stack.push(char)   # le

   start=0    # level
   if len(string) % 2 ==0:
        start=len(string) // 2
   else:
        start=len(string) // 2+1   # [3] el

   for char in string[start:]:    # el
        if char !=stack.pop():
             return False
   return True

if __name__ == "__main__":
      print(is_palindrome("level"))  
      print(is_palindrome("deed"))  
      print(is_palindrome("input"))  


      # 8분 시작