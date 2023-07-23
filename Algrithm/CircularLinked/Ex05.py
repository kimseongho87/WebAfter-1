# 리스트를 연결 리스트로 변경
class Node:
    def __init__(self):
        self.data=None
        self.link=None

# 출력함수
def print_nodes(head):
    current=head
    if current==None:
        return 

    print(current.data, end=' ')
    while current.link != head:
        current=current.link    
        print(current.data, end=' ')
    print()

# 데이터 삽입
def  insert(new_data, find_data=None):
    global memory, head, current, pre

    # 첫번째 노드
    if head.data == find_data:
        node=Node()
        node.data=new_data
        node.link=head

        last=head     # 다현 정연 쯔위 사나 지효
        while last.link != head:
            last=last.link
        last.link=node
        head=node
        return 

    # 중간 노드
    current=head
    while current.link !=head:
        pre=current
        current=current.link

        if current.data==find_data:
            node=Node()
            node.data=new_data
            node.link=current               # node.link=pre.link
            pre.link=node
            return 

    # 마지막 노드
    node=Node()
    node.data=new_data
    # current.link=node
    # node.link=head
    node.link=current.link
    current.link=node


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
        pre=node             # 사나
        node=Node()       # 지효
        node.data=data
        pre.link=node       # 사나--> 지효
        node.link=head
        memory.append(node)

    print_nodes(head)     # 다현 정연 쯔위 사나 지효

    insert("화사", "다현")
    print_nodes(head)  

    insert("솔라", "사나")
    print_nodes(head)  

    insert("문별")
    print_nodes(head)
  

