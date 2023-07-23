class Node:
    def __init__(self):
        self.data=None
        self.link=None


node1=Node()
node1.data="다현"
# node1.link=node1

node2=Node()
node2.data="정연"
node1.link=node2
# node2.link=node1

node3=Node()
node3.data="쯔위"
node2.link=node3
# node3.link=node1

node4=Node()
node4.data="사나"
node3.link=node4
# node4.link=node1

node5=Node()
node5.data="지효"
node4.link=node5
node5.link=node1

current=node1
print(current.data, end=' ')     # 다현
while current.link != node1:
    current=current.link               # 정연  쯔위 지효
    print(current.data, end=' ')     # 정연  쯔위  지효
print()

# 중간에 추가 : 다현 정연 쯔위 사나 지효 -- 다현 정연 [재남] 쯔위 사나 지효
new_node=Node()
new_node.data="재남"
new_node.link=node2.link
node2.link=new_node

current=node1
print(current.data, end=' ')     
while current.link != node1:
    current=current.link               
    print(current.data, end=' ')    
print()

# 삭제 : 다현 정연 재남 쯔위 사나 지효
node2.link=node3.link
del node3

current=node1
print(current.data, end=' ')
while current.link != node1:
    current=current.link
    print(current.data, end=' ')
print()

