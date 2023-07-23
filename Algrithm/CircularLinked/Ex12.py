class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

def find_node(head, k):   
    if head == None or k <=0:
        return None

    result=[]
    current=head
    for _ in range(k):
        result.append(current.data)
        current=current.next

        if current == head:
            break

    return result
        
if __name__ == "__main__":  
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(6)
    head.next.next.next.next.next.next=head

    print(find_node(head, 3))

