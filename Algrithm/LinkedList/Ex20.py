class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_value(head, target):     # 1시에 시작합니다.
    current=head

    while current != None:
        if current.data==target:
            return current
        current=current.next
    return None

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    target=3
    result=search_value(head, target)

    if result is not None:     # result != None
        print("노드가 찾아졌습니다",  result.data)
    else:
        print("해당 값이 존재하지 않습니다.")