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

# 데이터 삭제
def  delete(delete_data):               # 다현
    global memory, head, current, pre

    if head.data == delete_data:    # 다현 정연 쯔위 사나 지효
        current=head
        head=head.link                    #  정연
        last=head

        while last.link != current:
            last=last.link
        last.link=head
        del current

    current=head    # 다현 current, head
    while current.link != head:
        pre=current                               # 현재노드를 이전노드로
        current=current.link                  #  다음노드를 현재노드로

        if current.data == delete_data:
            pre.link=current.link
            del current
            return 

if __name__=="__main__":
    memory=[]
    head, current, pre=None, None, None
    data_array=["다현", "정연", "쯔위", "사나", "지효"]

    node=Node()
    node.data=data_array[0]
    head=node
    node.link=head
    memory.append(node)

    for data in data_array[1:]:
        pre=node             # 사나
        node=Node()       # 지효
        node.data=data
        pre.link=node       # 사나--> 지효
        node.link=head
        memory.append(node)

    print_nodes(head)     # 다현 정연 쯔위 사나 지효

    delete("다현")
    print_nodes(head)

    delete("쯔위")
    print_nodes(head)


 
  

