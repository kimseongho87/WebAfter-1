# 모든 데이터 빈도수

def binary_search(num, target):
      start=0
      end=len(num)-1

      while start <=end:
            mid=(start+end) // 2

            if num[mid]==target:
                  return mid          # idx
            elif num[mid] < target:
                  start=mid+1
            else:
                  end=mid-1

      return -1

if __name__ == "__main__":
      numbers=[30, 40, 50, 50, 60, 30, 70, 40, 80, 90, 30, 30]
      numbers.sort()                     
      uniqu=list(set(numbers))
      # print(numbers)
      # print(uniqu)

      for num in uniqu:
        count=0
        idx=0

        while idx != -1:            # [30, 30, 30, 30, 40, 40, 50, 50, 60, 70, 80, 90], 30
            idx=binary_search(numbers, num)

            if idx != -1:
                count +=1
                del(numbers[idx])

        print(num, count)

