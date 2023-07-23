class MyFriend:
    def __init__(self):
        self.katok=[]

    # 데이터 끝에 추가
    def add_data(self, data):
        self.katok.append(None)
        idx=len(self.katok)-1

        self.katok[idx]=data
        print(self.katok)

    # 데이터 삽입
    def insert_data(self, pos, data):
        if pos < 0 or pos > len(self.katok):
            print("데이터를 삽입할 범위를 벗어났습니다.")

        self.katok.append(None)
        idx=len(self.katok)-1
        # start:마지막idx     end:pos    step:-1

        for i in range(idx, pos, -1):
            self.katok[i]=self.katok[i-1]
            self.katok[i-1]=None

        self.katok[pos]=data     
        print(self.katok)
        

    # 데이터 삭제
    def delete_data(self, pos):
        if pos < 0 or pos >=len(self.katok):
            print("데이터를 삭제할 범위를 벗어났습니다.")
            return 
        
        self.katok[pos]=None
        idx=len(self.katok)
   
        # start:pos+1  end:마지막데이터   
        for i in range(pos+1, idx):
            self.katok[i-1]=self.katok[i]
            self.katok[i]=None

        del(self.katok[idx-1])
        print(self.katok)


if __name__=="__main__":
    friend=MyFriend()

    while True:
        choice=int(input("선택하세요: 1.추가 / 2.삽입 / 3.삭제 / 4.종료 : "))
        if choice==1:
            data=input("추가할 데이터:")
            friend.add_data(data)
        elif choice==2:
            pos=int(input("삽입할 위치:"))
            data=int(input("추가할 데이터:"))
            friend.insert_data(pos, data)
        elif choice==3:
            pos=int(input("삭제할 위치:"))
            friend.delete_data(pos)
        elif choice==4:
            exit()


          


      