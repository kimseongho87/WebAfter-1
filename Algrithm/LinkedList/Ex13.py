# 리스트를 연결 리스트로 변경
class Node:
    def __init__(self):
        self.data=None
        self.link=None

if __name__=="__main__":
      memory=[]
      head, current, pre=None, None, None
      data_array=["다현", "정연", "쯔위", "사나", "지효"]     # list

      node=Node()
      node.data=data_array[0]
      head=node
      memory.append(node)
      # print(memory)

      for data in data_array[1:]:     
           pre=node              #  기존 노드
           # print(pre.data)
           node=Node()        #  
           node.data=data     # 새로노드
           pre.link=node        #  기존링크 =새로노드
           memory.append(node)

      print(head.data)
      print(head.link.data)
      print(head.link.link.data)
      print(head.link.link.link.data)
      print(head.link.link.link.link.data)
      print()

      current=head
      print(current.data, end=' ')
      while current.link !=None:
           current=current.link
           print(current.data, end=' ')
      print()
     