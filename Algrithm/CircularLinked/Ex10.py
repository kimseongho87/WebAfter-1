class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

def calc(head):     # 37분
    current=head

    sum=0
    while True:
        # print(current.data)

        sum += current.data
        current=current.next

        if current == head:
            return sum


if __name__ == "__main__":  
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(55)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=head

    print(calc(head))    # 94