# 반복문 사용
katok=["다현", "정현", "쯔위", "사나", "지효", "모모"]
katok.append(None)
print(katok, len(katok))   # 7

idx=len(katok)-1       # 6 마지막번지     
print(idx)       
pos=2                       # 2 삽입 번지

for i in range(idx, pos, -1):                # 6, 2, -1
    print(idx, pos)
    katok[i]=katok[i-1]                       # k[6] N모모 = 모모 k[5] / k[5] 사나 = k[4] 사나  / k[4]  None 쯔위 = 쯔위 k[3]
    katok[i-1]=None                          # k[5]=None   / k[4]=None / k[3]=None
    print(katok)

katok[pos]="솔라"
print(katok)

# 13분 시작합니다.