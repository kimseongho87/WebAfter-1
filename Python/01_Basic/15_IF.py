# 제어문 - 조건문, 반복문
# if - 형식1)
x=15
if x > 10 :          # 15 > 10
   print("10보다 큰수입니다")

print("hahahahaha \n\n")

y=20
if y >10 and y < 30:
   y += 200
   print(y)

su=20
if su%2==0:
   print("짝수입니다")

if su%2 !=0:
   print("홀수입니다")

print("\n\n")

# if - 형식2)
if su%2==0:
   print("짝수입니다")
else:
   print("홀수입니다")

if su > 0 :
   su +=100
   print(su, "양수입니다")
else:
   su *=200
   print(su, "음수입니다.")

print("\n\n")

# if - 형식3)
money=2000
if money >= 3000:
   print("택시를 이용하세요")
elif money >= 2000:
   print("버스를 이용하세요")
else:
   print("도보를 이용하세요")

print("\n")

jumsu=85
if jumsu >=90:
   print("A등급")
elif jumsu >=80:
   print("B등급")
elif jumsu >=70:
   print("C등급")
else:
   print("D등급")

print("\n")

# 중첩 if문  A+ A0 A-
score=84
grade=None

if score >=90:
   if score >=97:
      grade="A+"
   elif score >=94 and score <= 96 :
      grade="A0"
   elif score >=90:
      grade="A-"
elif score >=80:
     if score >=87:
          grade="B+"
     elif score >=84 and score <= 86 :
          grade="B0"
     elif score >=80:
          grade="B-"
elif score >=70:
      if score >=77:
         grade="C+"
      elif score >=74 and score <= 76 :
         grade="C0"
      elif score >=70:
         grade="C-"
elif score < 70:
         grade="재수강"

print("학점:", score, "\t", grade)










