class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def empty(self):
        return self.head is None

    def value_at(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Index out of bounds")
        return current.value

    def push_front(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def pop_front(self):
        if self.head is None:
            raise IndexError("Pop from empty list")
        value = self.head.value
        self.head = self.head.next
        return value

    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop_back(self):
        if self.head is None:
            raise IndexError("Pop from empty list")
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        current = self.head
        while current.next.next:
            current = current.next
        value = current.next.value
        current.next = None
        return value

    def front(self):
        if self.head is None:
            raise IndexError("Empty list")
        return self.head.value

    def back(self):
        if self.head is None:
            raise IndexError("Empty list")
        current = self.head
        while current.next:
            current = current.next
        return current.value
