# 클래스로 작성
class Node:
    def __init__(self, data=None):
        self.data=data
        self.link=None

class LinkedList:
    # 생성자 : 해당 클래스 초기화 작업
    def __init__(self):
        self.head=None

    # 데이터 입력   
    def add(self, data):      # 지효
        node=Node(data)   # 지효.data=지효 / 지효link=None

        if self.head == None:
            self.head=node
            node.link=self.head
        else :
            current=self.head     # current, head = 다현
            while current.link !=self.head:    # 사나 - > head
                current=current.link      # 사나

            current.link=node        # 사나 --> 지효
            node.link=self.head     # 다현, 정연, 쯔위, 사나, 지효

    # 출력
    def print_nodes(self):
        current=self.head
        if current==None:
            return
        
        print(current.data, end=' ')
        while current.link != self.head:
            current=current.link
            print(current.data, end=' ')
        print()

     # 삽입 - 첫번째, 중간, 마지막
    def insert(self, new_data, find_data=None):    # 문별
        node=Node(new_data)         # 문별.data=문별, 문별.link=None

        if self.head.data == find_data:     # 첫번째
            node.link=self.head
            last=self.head    

            while last.link != self.head:     
                last=last.link
            last.link=node
            self.head=node
        else:
            current=self.head    
            while current.link !=self.head:     # 화사 다현 [솔라] 정연 쯔위 사나 지효
                pre=current                    # 다현
                current=current.link       # 정연
                if current.data == find_data:   # 정연
                    node.link=current     # pre.link
                    pre.link=node
                    return 
                
            current.link=node
            node.link=self.head
                    
   # 삭제 - 첫번째, 그외
    def delete(self, delete_data):     # 화사 다현 솔라 정연 쯔위 사나 지효 문별
         if self.head.data == delete_data:
             current=self.head            # 화사
             self.head=self.head.link   # 다현
             last=self.head                  # 다현

             while last.link !=current:    # 솔라 != 화사
                 last=last.link
             last.link=self.head
             del current
         else :  
              current=self.head
              while current.link != self.head:
                  pre=current
                  current=current.link
                  if current.data==delete_data:
                     pre.link=current.link
                     del current
                     return
      
      # 검색
    def search(self, find_data):
        current=self.head

        if current.data==find_data:
            return current
        else:   
            while current.link !=self.head:
               current=current.link
               if current.data==find_data:
                  return current              
       
        return Node()      # 2시 시작합니다.
    
if __name__ == "__main__":
    linked=LinkedList()
    linked.add("다현")
    linked.print_nodes()

    linked.add("정연")
    linked.add("쯔위")
    linked.add("사나")
    linked.add("지효")
    linked.print_nodes()
    print()

    linked.insert("화사", "다현")
    linked.print_nodes()

    linked.insert("솔라", "정연")
    linked.print_nodes()

    linked.insert("문별")         
    linked.print_nodes()         # 화사 다현 솔라 정연 쯔위 사나 지효 문별

    linked.delete("화사")
    linked.print_nodes()    

    linked.delete("쯔위")
    linked.print_nodes()    

    print("\n검색출력*****")
    result=linked.search("다현")
    print(result.data)

    result=linked.search("사나")
    print(result.data)

    result=linked.search("쯔위")
    print(result.data)
