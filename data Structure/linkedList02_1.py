##self.head란 가장 첫번째 데이터의 주소값
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next =next

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def delete(self,data):
        if self.head == '':
            print("노드가 없다") 
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


list1 =NodeMgmt(0)

for index in range(1,10):
     list1.add(index)

list1.delete(2)
list1.desc()

