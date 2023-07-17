"""
   알고리즘 하기 위한 선행 학습 :  리스트(배열) /연결리스트, 스택, 큐
                                                       검색 : 선형검색, 이진검색
                                                       정렬 :  버블, 선택, 삽입, 퀵
   선행학습 전 : 함수, 기본클래스,  제어문(반복문, 조건문)
"""

# 실습문제 - 랜덤하게 0~200 사이의 숫자 20개 생성한 후  오름(내림) 차순으로 정렬하도록 코드를 작성하고, 몇번만에 정렬했는지
#                    횟수를 출력하기 

import random

def quick_sort(arr):
    if len(arr) <=1:
        return arr, 0
    
    pivot=arr[len(arr)//2]
    left, right=[], []
    count=0

    for num in arr:
        count +=1
        if num > pivot:
            left.append(num)
        elif num < pivot:
            right.append(num)

    sorted_left, left_count = quick_sort(left)
    sorted_right, right_count = quick_sort(right)
    count += left_count + right_count

    return sorted_left + [pivot] + sorted_right, count
   
if __name__=="__main__":
    arr=[random.randint(0, 200) for _ in range(0, 20)]
    # print(arr, len(arr))

    result_sort, count=quick_sort(arr)
    print(result_sort)
    print(count)