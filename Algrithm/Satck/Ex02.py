def check_gwallho(s):
      print(s)     # (  / ( ) / ( (  )  / )
      stack=[]

      for i in range(len(s)):  
            if s[i] == '(':
                  stack.append(s[i])    # (   / (
            elif s[i] == ')':                 #     / )
                  if len(stack)==0:
                        return False
                  stack.pop()
                  
      if len(stack)==0:
            return True
      else:
            return False


print(check_gwallho('('))     # false
print(check_gwallho('()'))    # true
print(check_gwallho('(()'))    # false
print(check_gwallho(')'))    
print(check_gwallho('((()))'))   

# 1시 시작

