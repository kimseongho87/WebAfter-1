class Node:
    def __init__(self):
        self.data=None
        self.link=None

if __name__=="__main__":
    node1=Node()
    node1.data="다현"

    node2=Node()
    node2.data="정현"
    node1.link=node2

    node3=Node()
    node3.data="쯔위"
    node2.link=node3

    node4=Node()
    node4.data="샤니"
    node3.link=node4