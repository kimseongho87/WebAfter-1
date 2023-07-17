def count_down(n):   # 0
    if n==0:
        print("발사")
    else:
        count_down(n-1)      # n:5  4  / n:4   3  / n:3  2  / n:2  1  / n:1  0
        print(n)     

count_down(5)
print()

def print_Start(n):         # 4
    if n > 4: 
        print_Start(n-1)     #  n:5  4  / n:4  3
        print("*" * n)
      
if __name__ == "__main__":
    print_Start(5)




