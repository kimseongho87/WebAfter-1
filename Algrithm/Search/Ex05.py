import random

def binary_search(product, target):
    start=0
    end=len(product)-1

    while start <= end:
        mid=(start + end) // 2

        if product[mid]==target:     
             return mid
        elif product[mid] < target: 
            start=mid+1
        else:
            end=mid-1
    return -1

if __name__ == "__main__":
    data_list=["바나나맛 우유", "레쓰비캔커피", "츄파춥스", "도시락", "삼다수", "코카콜라", "삼각김밥"]
    sell_list=[random.choice(data_list) for _ in range(20)]
    # print(sell_list, len(sell_list))

    sell_list.sort()
    print("오늘 판매된 물건:%s\n"%sell_list)

    product_list=list(set(sell_list))
    print("오늘 판매된 물품종류:%s\n"%product_list)

    count_list=[]
    for product in product_list:
        count=0
        idx=0

        while idx != -1:
            idx=binary_search(sell_list, product)
            if idx != -1:
                count += 1
                del(sell_list[idx])

        count_list.append((product, count))

print(count_list)



    
