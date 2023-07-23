# 노드 검색

class Node:
    def __init__(self):
        self.data=None
        self.link=None

# 출력 함수
def print_nodes(head):
    current=head
    if current == None:
        return

    print(current.data, end=' ')
    while current.link != None:
        current=current.link
        print(current.data, end=' ')
    print()

# 검색
def search(find_data):
    global memory, head, current, pre

    current=head
    if current.data==find_data:
        return current
    
    while current.link != None:
        current=current.link
        if current.data == find_data:
            return current
        
    return Node()   # 빈 노드 리턴

if __name__ == "__main__":
    memory=[]
    head, current, pre=None, None, None
    data_array=["다현", "정연", "쯔위", "사나", "지효"]

    node=Node()
    node.data=data_array[0]
    memory.append(node)
    head=node

    for data in data_array[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.link=node
        memory.append(node)         

    print_nodes(head)       # 다현 정연 쯔위 사나 지효

    find_node=search("다현")
    print(find_node.data, "찾았습니다.")     # 다현

    find_node=search("쯔위")
    print(find_node.data, "찾았습니다.")        # 쯔위

    find_node=search("재남")
    print(find_node.data)     # none

    # 4시 시작합니다.

    



    

