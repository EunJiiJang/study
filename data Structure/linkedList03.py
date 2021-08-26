class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev = prev
        self.next = next
        self.data = data

class NodeMgmt:
    def __init__(self,data):
        self.head =Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head =Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node=node.next

    def search(self,data):
        node =self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_tail(self,data):
        node =self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self,data,b_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != b_data:
                node = node.prev
                if node == None:
                    return False

            new = Node(data)
            b_new = node.prev
            b_new.next = new
            new.prev = b_new
            new.next = node
            node.prev = new
            return True

d_list = NodeMgmt(0)
for data in range(1,10):
    d_list.insert(data)
# d_list.desc()

# node3 = d_list.search_tail(3)
# print(node3.data)

d_list.insert_before(1.5,2)
d_list.desc()