# 리스트를 연결 리스트로 변경
class Node:
    def __init__(self):
        self.data=None
        self.data=None

if __name__=="__main__":
    memory=[]
    head, current, pre=None, None, None
    data_array=["다현", "정연", "쯔위", "사나", "지효"]

    node=Node()
    node.data=data_array[0]
    head=node
    node.link=head
    # print(head.data, head.link)
    memory.append(node)

    for data in data_array[1:]:
        pre=node                     # 사나
        node=Node()
        node.data=data    # 지효
        pre.link=node       # 사나 = 지효
        node.link=head
        memory.append(node)

    current=head
    print(current.data, end=' ')
    while current.link != head:
        current=current.link    
        print(current.data, end=' ')
    print()