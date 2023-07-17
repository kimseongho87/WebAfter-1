# 리스트 정렬
su=[3, 8, 2, 7, 6, 10, 9]

sorted_su=sorted(su)                            # 파이썬 내장함수 - 원본에 영향 안줌
print(su)
print(sorted_su)       

reverse_su=sorted(su, reverse=True)    # 정렬의 순서를 반대로
print(reverse_su, "\n")

su.sort()                                                 # list 제공 sort() 함수 - 원본에 영향 줌
print(su)

su.sort(reverse=True);                           #  정렬의 순서를 반대로
print(su, "\n")


# 문자열 정렬
fruit=["Apple", "Banana", "Orange", "Pineapple", "Mango"]
fruit.sort()
print(fruit)                                                # fruit.sort(reverse=True)

fruit=["Apple", "Banana", "Orange", "Pineapple", "Mango"]
sorted_fruit = sorted(fruit, key=len, reverse=True)                              # 문자의 길이로 정렬
print(sorted_fruit)

fruit.sort(key=len, reverse=True)
print(fruit, '\n')

# dic 정렬
person=[{'name':'John', 'score':83}, {'name':'paul', 'score':92}]
sorted_person = sorted(person, key=lambda x: x['name'])    
print(sorted_person)

person.sort(key=lambda x: x['score'], reverse=True)
print(person, "\n")