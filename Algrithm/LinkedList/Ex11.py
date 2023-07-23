class Node:
    def __init__(self):
        self.data=None
        self.link=None

if __name__=="__main__":
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

    current=node1
    print(current.data, end=' ')          # 다현 정연 쯔위 사나 지효
    while current.link != None:      # 지효 링크
        current=current.link             #  지효=지효
        print(current.data, end=' ')   #  지효
    print("\n")

    # 데이터 추가
    # 다현 정연 쯔위 사나 지효
    node6=Node()
    node6.data="재남"
    node6.link=node2.link
    node2.link=node6

    current=node1
    print(current.data, end=' ')
    while current.link != None:
        current=current.link
        print(current.data, end=' ')
    print("\n")

   # 다현 모모 정연 재남 쯔위 샤니 지효   
    node7=Node()
    node7.data="모모"
    node7.link=node1.link
    node1.link=node7

    current=node1
    print(current.data, end=' ')
    while current.link != None:
        current=current.link
        print(current.data, end=' ')
    print("\n")
