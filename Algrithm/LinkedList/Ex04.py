# 함수를 이용해서 중간에 데이터 삽입
def insert_data(pos, friend, katok):
      if pos < 0 or pos > len(katok):
            print("데이터를 삽입할 범위를 벗어났습니다.")

      katok.append(None)    # ['다현', '정현', '솔라', '쯔위', '사나', '지효',None]
      idx=len(katok)-1           # 6

      for i in range(idx, pos, -1):                 #  6, 6
            katok[i]=katok[i-1]                      
            katok[i-1]=None                          
            print(katok)

      katok[pos]=friend    # ['다현', '정현', '솔라', '쯔위', '사나', '지효',문별]
      print(katok)

if __name__=="__main__":
      katok=["다현", "정현", "쯔위", "사나", "지효"]
      insert_data(2, '솔라', katok)
      insert_data(6, '문별', katok)