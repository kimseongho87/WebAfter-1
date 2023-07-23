"""
   1. 선형 리스트 또는 배열 : random access 가능,  추가/삭제 시간 많이 걸린다. 즉 오버헤드 발생한다.
   2. 연결 리스트 (LinkedList)
         - random access 불가능
         - 추가/삭제 시 오버헤드가 발생 안함
         - 종류 : 단일 연결 리스트(Singly Linked List),  이중 연결 리스트(Dobluy Linked List), 원형 연결리스트 (Circular Linked List)
"""

# 노드 생성, 연결
class Node:
    def __init__(self):
        self.data=None
        self.link=None

if __name__ == "__main__":
    node1=Node()       # head
    node1.data="다현"
    print(node1.data, node1.link)

    node2=Node()
    node2.data="정연"
    print(node2.data, node2.link)
    print()

    node1.link=node2
    print(node1.data, node1.link)
    print(node2.data, node2.link)
    print()

    print(node1.data, end=' ')
    print(node1.link.data, end= ' ')


