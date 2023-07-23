class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

def calc(head):
    current=head

   #  while current.next != head:
   #      print(current.data)    # 5가 안나온다
   #      current=current.next

    result=[]
    while True:
        # print(current.data)

        if current.data%2 == 0:
            result.append(current.data)
        current=current.next

        if current == head:
            break
        
    return result



if __name__ == "__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(55)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=head

    print(calc(head))