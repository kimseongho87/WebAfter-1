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
def  search(find_data):               # 다현
    global memory, head, current, pre

    current=head    # 다현
    if current.data==find_data:
        return current
    else :
        while current.link != head:
            current=current.link
            if current.data == find_data:
                return current
            
    return  Node()     # None
    
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

    print_nodes(head)       # 다현 정연 쯔위 사나 지효

    print("\n데이터 검색")
    find_node=search("다현")
    print(find_node.data)     # 다현

    find_node=search("쯔위")
    print(find_node.data)

    find_node=search("문별")
    print(find_node.data)

 
  

