class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def calc(head):
    current=head

    result=[]
    while current != None:     #   10, 20
        if current.data > 10:
            result.append(current.data)
        current=current.next    # 20

    return result
        
if __name__ == "__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(55)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)

    print(calc(head))