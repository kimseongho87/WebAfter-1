# 함수 이용해서 중간 데이터 삭제
def  delete_data(pos, katok):
    if pos < 0 or pos > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return 
    
    idx=len(katok)   # start:post+1, end:마지막번지
    katok[pos]=None

    for i in range(pos+1, idx):
        katok[i-1]=katok[i]
        katok[i]=None

    del(katok[idx-1])           #  배열의 맨 마지막 위치에 삭제
        

if __name__=="__main__":
    katok=["다현", "정연", "쯔위", "사나", "지효"]
    delete_data(1, katok)  
    print(katok)  
    delete_data(3, katok)   
    print(katok)    