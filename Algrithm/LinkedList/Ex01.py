# 선형 리스트 --> 연결 리스트  --> 원형 리스트 

# 맨뒤에 데이터 삽입
katok=[]
katok.append(None)
print(katok, len(katok))     # 1

katok[len(katok)-1]="모모"     #  katok[0] = "모모"
print(katok)

katok.append(None)
print(katok)
katok[len(katok)-1]="정현"
print(katok)

# 함수를 활용해서 맨뒤에 삽입
katok=[]
def add_data(friend):         # 다현, 정연
    katok.append(None)     # None, None
    klen=len(katok)-1          # 다현 None
    katok[klen]=friend         # 다현 정연

if __name__=="__main__":
    add_data("다현")
    add_data("정연")
    add_data('쯔위')
    add_data('사나')
    add_data('지효')
    print(katok)