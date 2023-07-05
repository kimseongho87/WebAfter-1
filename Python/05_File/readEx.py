# 파일 --> 입력

# 경로 :  C:\Users\JMH\Desktop\teacher\workspace\Python\05_File\readEx.py
# 방법1) path="C:/Users/JMH/Desktop/teacher/workspace/Python/05_File\input.txt"

path="C:\\Users\\JMH\\Desktop\\teacher\\workspace\\Python\\05_File\\input.txt"

# Ex1)
file=open(path, "r", encoding="UTF-8")     # UTF-8 전세계문자, 한글 euc-kr 
data=file.read()                # 모든 내용을 읽는다
print(data)
file.close()
print()

# Ex2-1)
file=open(path, "r", encoding="UTF-8")
line=file.readline()             # 한줄만 출력
print(line)
file.close()
print()

# Ex2-2)
file=open(path, "r", encoding="UTF-8")
while True:
    line=file.readline()

    if line !="":
        print(line, end="")
    else:
        break
file.close()
print()

# Ex-3)
file=open(path, "r", encoding="UTF-8")
lines=file.readlines()          # 한줄씩 읽어와서 리스트에 반환
print(lines)
file.close()

for line in lines:
    print(line, end="")

print("\n\n")

# Ex-4)  close() 자동으로 된다.
with open(path, "r", encoding="UTF-8") as file:
    # data=file.read()
    # data=file.readline()
    data=file.readlines()
    print(data)


# Ex-5)
with open("output4.txt", "r", encoding="UTF-8") as file:
    data=file.readlines()
    print(data)
    



