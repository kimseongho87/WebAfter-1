# 중간 데이터 삽입 - 2번지 솔라 삽입
katok=["다현", "정현", "쯔위", "사나", "지효", "모모"]
katok.append(None)
print(katok)

katok[6]=katok[5]
katok[5]=None
print(katok)

katok[5]=katok[4]
katok[4]=None
print(katok)

katok[4]=katok[3]
katok[3]=None
print(katok)

katok[3]=katok[2]
katok[2]=None
print(katok)

katok[2]="솔라"
print(katok)