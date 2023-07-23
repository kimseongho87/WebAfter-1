class Node:
    def __init__(self):
        self.data=None
        self.link=None

if __name__ == "__main__":
    node1=Node()
    node1.data="다현"

    node2=Node()
    node2.data="정연"
    node1.link=node2

    node3=Node()
    node3.data="쯔위"
    node2.link=node3

    node4=Node()
    node4.data="사나"
    node3.link=node4

    node5=Node()
    node5.data="지효"
    node4.link=node5

    print(node4.data, node4.link)
    print(node5.data, node5.link)
    print()

    print(node1.data, end=' ')
    print(node1.link.data, end=' ')
    print(node1.link.link.data, end=' ')
    print(node1.link.link.link.data, end=' ')
    print(node1.link.link.link.link.data, end=' ')
    print()

    # 반복문 사용   다현 정연 쯔위 사나 지효
    current=node1                                 # head
    print(current.data, end=' ')               #  다현
    while current.link != None:     # 지효링크
        current=current.link            #  지효=지효
        print(current.data, end=' ')       # 지효

