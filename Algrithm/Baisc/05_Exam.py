# 내장함수를 직접 작성

def my_sum(data):
    hap=0
    for i in range(len(data)):
        hap=hap+data[i]
    return hap

def my_max(data):
    max=data[0]                     # 11
    for i in range(len(data)):
        if max < data[i]:            # 12 < 14
            max=data[i]              # 12
    return max

def my_min(data):
    min=data[0]
    for i in range(len(data)):
        if min > data[i]:
            min=data[i]    
    return min

def my_len(data):
   count=0
   for i in data:
        count +=1
   return count

if __name__ == "__main__":
   su=[11, 12, 14, 55, 77, 99, 1, 2] 
   print(my_sum(su))
   print(my_max(su))
   print(my_min(su))
   print(my_len(su))