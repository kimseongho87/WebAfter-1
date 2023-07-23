# 노드 삭제 

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

# 삭제
def delete(delete_data):
    global memory, head, current, pre

    # 첫번째 노드 삭제
    if head.data==delete_data:     # ["다현", "정연", "쯔위", "사나", "지효"]
        current=head                      # 다현=다현
        head=head.link                   # 정연
        delete(current)
        return 
    
    # 첫번째 노드 이외 삭제
    current=head
    while current.link != None:
        pre=current
        current=current.link

        if current.data==delete_data:
            pre.link=current.link
            del(current)
            return

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

    print_nodes(head)

    delete('다현')
    print_nodes(head)

    delete("쯔위")
    print_nodes(head)



    

