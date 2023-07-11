from StackFixed import Stack

def my_max(stack):
    max_value=stack.pop()
    
    # while stack.is_full():
    while not stack.is_Empty():
         item=stack.pop()
         if item > max_value:
              max_value=item
    return max_value
         
def my_sum(stack):
     pass           # 13

if __name__ == "__main__":
      stack=Stack(5)
      stack.push(5)
      stack.push(2)
      stack.push(80)
      stack.push(1)
      stack.push(10)

      # print(my_max(stack))