# 중간 데이터 삭제 - 반복문
katok=["다현", "쯔위", "사나", "지효", "모모"]

pos=1                # 쯔위 삭제
katok[pos]=None

# start:2     end:4     step:1
for i in range(pos+1, len(katok)):    # ["다현",  None, "사나", "지효", "모모"]
      katok[i-1]=katok[i]                    # ["다현",  "사나", "사나", "지효", "모모"]     
      print(katok)
      katok[i]=None                          #  ["다현",  "사나", None, "지효", "모모"] 
      print(katok)

del(katok[len(katok)-1])            
print("\n", katok)