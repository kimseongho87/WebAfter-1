class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

def calc(head):     
    current=head

    max=0                   # head.data
    while True:
        if max < current.data:
            max=current.data
        current=current.next

        if current == head:
            return max
        
if __name__ == "__main__":  
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(55)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=head

    print(calc(head))      # 가장 큰값출력        