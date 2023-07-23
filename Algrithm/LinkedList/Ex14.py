# 노드 클래스 
class Node:
    def __init__(self):
        self.data=None
        self.link=None

 # 출력함수
def print_nodes(head):
    current=head
    if current==None:
        return 

    print(current.data, end=' ')   
    while current.link != None:
        current=current.link
        print(current.data, end=' ')
    print() 

# 추가 함수
def insert(new_data, find_data=None):
   global memory, head, current, pre

   # 첫번째 노드 삽입
   if head.data==find_data:
       node=Node()
       node.data=new_data    # 화사
       node.link=head             # 화사.링크 = 다현
       head=node                    # 헤드 = 화사

   # 중간 노드 삽입    
   current=head                             # 화사 다현 정연 쯔위 사나 지효
   while current.link != None:        
       pre=current                            # 화사 다현  정연 쯔위
       current=current.link                # 다현 정연  쯔위 사나
       if current.data == find_data:
           node=Node()                                   
           node.data=new_data
           node.link=current
           pre.link=node                   # 화사 다현 정연 쯔위 솔라 사나 지효
           return 

   # 마지막 노드 삽입    
   node=Node()
   node.data=new_data   
   current.link=node     
 

if __name__=="__main__":                  # 노드 추가 (처음, 중간, 마지막)
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

    # 처음 노드 추가 : 다현 정연 쯔위 사나 지효
    insert("화사", "다현")
    print_nodes(head)        # 화사 다현 정연 쯔위 사나 지효

    insert("솔라", "사나")   # 화사 다현 정연 쯔위 솔라 사나 지효
    print_nodes(head)

    insert("문별")
    print_nodes(head)

    # 5분 시작합니다.

