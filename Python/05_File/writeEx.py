# 내용 --> 파일 출력

# Ex1) 
path="C:/Users/JMH/Desktop/teacher/workspace/Python/05_File/output1.txt"    # output1.txt 자동으로 생긴다.
file=open(path, "w", encoding="UTF-8")
file.write("작성합니다. \n")
file.write("반가워요 \n")
file.write("How are you? \n")
file.close()

# Ex2)
path="C:/Users/JMH/Desktop/teacher/workspace/Python/05_File/output2.txt"
data=["콜린 벨(61) 한국 여자 축구대표팀 감독이 2007년생 혼혈 선수 케이시 페어(PDA)를 뽑은 이유를 설명했다. \n",
          "대한축구협회(KFA)는 오는 20일 개막하는 '2023 FIFA 호주·뉴질랜드 여자월드컵'에 \n"
          "나설 여자 축구대표팀 최종 엔트리 23명과 예비 멤버 2명을 5일 발표했다. \n"]
file=open(path, "w", encoding="utf-8")
file.writelines(data)
file.close()

# Ex3)
path="C:/Users/JMH/Desktop/teacher/workspace/Python/05_File/output3.txt"
with open(path, "w", encoding="utf-8") as file:
    file.writelines(data)

# Ex4) workspace 폴더 저장
with open("output4.txt", "w", encoding="utf-8") as file:
    file.writelines(data)

# Ex5) 추가
with open("output4.txt", "a", encoding="utf-8") as file:
    file.write("추가합니다. \n")