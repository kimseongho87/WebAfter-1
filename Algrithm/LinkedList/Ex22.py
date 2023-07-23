class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(head, value):
     if head == None:
        return None

     if head.data < value:
       head=head.next
   
     current = head
     pre=current
     while current != None:
        if current.data < value:
            pre.next = current.next
            # del current  완전 삭제되어 반복문을 수행할 수 없음
        else:
            pre = current
        current = current.next
     return head
      
# 2시 15분 시작
if __name__ == "__main__":
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(1)

    result=delete(head, 3)

    current = result    
    while current != None:
         print(current.data, end=' ')
         current = current.next
    print()