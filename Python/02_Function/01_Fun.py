#  함수
#  입력값과 결과값에 따른 함수 형태

# CASE-1) 인수:X, 리턴:X
# Ex1)
def disp():
    print("Hello")

disp()

# Ex2)
def sub():
    print("Sub Function")

for i in range(1, 6):
    sub()

print()

# Ex3)
def aa():
    print("aa Function")

def bb():
    print("bb Function")

def cc():
    print("cc Funciton")

su=int(input("수:"))
if su==1:
    aa()
elif su==2:
    bb()
elif su==3:
    cc()


