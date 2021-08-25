##링크드 리스트는 데이터의 사이즈를 선언하지 않아도 됨
##데이터+주소 =node(노드) 지칭함

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 =Node(1)
node2 =Node(2)
node1.next = node2
head = node1

for index in range(1,10):
    add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)