class Node:
    def __init__(self, data):   # 다현
        self.data=data
        self.link=None

class LinkedList:
    def __init__(self):
        self.head=None

    # 추가 
    def add(self, data):
        node=Node(data)                   #   다현, 정연, 쯔위, 사나
                                                        
        if self.head == None:
            self.head=node                     #   다현 = head
        else :
             current = self.head                #   
             while current.link != None:    #   
                  current = current.link        #    
             current.link=node                  #  link None = 데이터 추가 

       # 출력
    def print_nodes(self):
        current=self.head
        if current == None:
            return 
        
        print(current.data, end=' ')
        while current.link != None:
            current=current.link
            print(current.data, end=' ')
        print()    

        # 삽입
    def insert(self, new_data, find_data=None):     # 다현 정연 쯔위 사나 지효 화사
      
        if self.head.data == find_data:                      # 첫번째 데이터 : head 바뀐다.
            node = Node(new_data)         
            node.link=self.head
            self.head=node
            return 
        
        # 화사 다현 [솔라] 정연 쯔위 사나 지효
        current=self.head
        while current.link != None:
            pre=current
            current=current.link
            if current.data == find_data:
                node=Node(new_data)
                node.link=current
                pre.link=node
                return 
            
        node=Node(new_data)               # 마지막 노드 삽입
        current.link=node

    # 삭제
    def delete(self, delete_data):
        if self.head == None:
            return
        
        if self.head.data == delete_data :
            current=self.head                     # 화사
            self.head=self.head.link            # 다현
            del current
            return 
        
        current=self.head                       # 다현 솔라 정연 [쯔위] 사나 지효 문별
        while current.link != None:
            pre=current
            current=current.link
            if current.data == delete_data:
                pre.link=current.link
                del current
                return 
            
            # 5분에 시작

if __name__ == "__main__":
    linked=LinkedList()
    linked.add("다현")               # 다현 노드(data, link) / head
    linked.add("정연")
    linked.add("쯔위")
    linked.add("사나")
    linked.add("지효")
    linked.print_nodes()              # 다현 정연 쯔위 사나 지효

    linked.insert("화사", "다현")    
    linked.print_nodes()              # 화사 다현 정연 쯔위 사나 지효

    linked.insert("솔라", "정연")
    linked.print_nodes()

    linked.insert("문별")
    linked.print_nodes()

    linked.delete("화사")
    linked.print_nodes()

    linked.delete("쯔위")
    linked.print_nodes()






