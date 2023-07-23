# 원형 연결 리스트 (Circular Linked List)

# 노드 생성, 출력
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
node2.link=node1

print(node1.data)
print(node1.link.data)
print()

print(node2.data)
print(node2.link.data)
