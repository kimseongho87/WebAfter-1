# 간단하게 작성
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def disp():
    global head

    if head == None:
        return 
    
    current=head
    while current !=None:
        print(current.data, end=' ')    # 2
        current=current.next             #  3
    print()

def insert(new_data, find_data=None):
    global head

    node=Node(new_data)
    current=head

    if current.data == find_data:
        node.next, head=head, node
        return 
    else:     # 88 1 2 [77] 3 4 5
        while current != None:
            if current.data==find_data:
                node.next, current.next=current.next, node
                return 
            elif current.next == None:
                current.next=node
                return 
            current=current.next    
            
def delete(delete_data):
    global head

    current=head
    if current.data==delete_data:
        head=current.next
        del current
    else:
        while current != None:    # 1 2 77 3 [4] 5 99
            pre=current
            current=current.next
      
            if current.data == delete_data:
                pre.next=current.next
                del current
                return
            
            # current=current.next   삭제


if __name__ == "__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    disp()

    insert(88, 1)
    disp()

    insert(77, 2)
    disp()

    insert(99)
    disp()

    delete(88)
    disp()

    delete(4)
    disp()

    delete(3)
    disp()