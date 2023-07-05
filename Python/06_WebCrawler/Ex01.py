import requests
import sys
from bs4 import BeautifulSoup

def get_subject():
    req=requests.get("https://basicenglishspeaking.com/daily-english-conversation-topics/")
    html=req.text
    # print(html)

    soup=BeautifulSoup(html, "html.parser")
    divtag=soup.findAll("div", {'class':'tcb-flex-col'})
    # print(len(divtag))

    subjects=[]
    for div in divtag:       # 3
        atag=div.findAll("a")
        # print(len(atag))

        for a in atag:
            subjects.append(a.text)

    return subjects

def once_conversation():
     input_data=input("대화 주제별 이름:")     # Family, Books, Travel

     req=requests.get("https://basicenglishspeaking.com/" +  input_data)
     html=req.text
     # print(html)
     soup=BeautifulSoup(html, "html.parser")

     question_answer=soup.findAll("div", {'class':'sc_player_container1'})
     # print(len(question_answer))

     for qna in question_answer:
          if question_answer.index(qna) %2==0:
               question=qna.next_sibling
               print("질문:", question, end='')
          else :
               answer=qna.next_sibling
               print("답변:", answer)
          print()

def  all_conversation(subjects):      # 주제
         
         for sub in subjects:
               req=requests.get("https://basicenglishspeaking.com/" + sub)
               html=req.text
               soup=BeautifulSoup(html, "html.parser")

               question_answer=soup.findAll("div",  {'class':'sc_player_container1'})
               # print(len(question_answer))

               for qna in question_answer:
                     if question_answer.index(qna) %2 ==0:
                           question=qna.next_sibling
                           print("질문:", question, end=' ')
                     else:
                           answer=qna.next_sibling
                           print("답변:", answer)
                     print()
                  
if __name__ == "__main__":
    choice=int(input("1.전체 영어 대화 주제 출력 / 2. 대화별 내용 출력 / 3. 대화별 전체 내용 출력 / 4. 파일 저장 / 99.종료 : "))

    if choice==1:
            subjects=get_subject()
            print("총개수는 %d 입니다."%len(subjects))

            for index, subject in enumerate(subjects):
               print(index+1, subject)

    elif choice==2:
            once_conversation()

    elif choice==3:
            subjects=get_subject()    # 대화 주제
            all_conversation(subjects)

    elif choice==4:
            subjects=get_subject()

            with open("subject.txt", "w", encoding="UTF-8") as file:
                  # file.writelines(subjects)

                  for index, subject in enumerate(subjects):
                        data=str(index+1) + " " + subject + "\n"
                        file.write(data)

          # 4시 5분 시작
    elif choice==99:
         sys.exit()



