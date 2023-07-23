class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 중복값 제거 - 15분까지 문제 풀기
def calc(head):
    current=head

    result=set()
    while current != None:
        result.add(current.data)
        current=current.next

    return list(result)


if __name__ == "__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(1)
    head.next.next.next.next.next.next=Node(2)

    print(calc(head))
