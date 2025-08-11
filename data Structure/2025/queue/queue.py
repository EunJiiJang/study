# implement using linked-list, with tail pointer:
#     enqueue(value) - adds value at a position at the tail
#     dequeue() - returns value and removes least recently added element (front)
#     empty()
# Implement using a fixed-sized array:
#     enqueue(value) - adds item at end of available storage
#     dequeue() - returns value and removes least recently added element
#     empty()
#     full()
from collections import deque

from problem.etc.sugarDelivery import value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

        if not self.head:
            return None

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:#가장앞의 값을 뽑고나서 다음값을 넣었는데 다음값이 없는경우에 해당
            self.tail = None
        return value

    def empty(self):
        return self.head is None

class ArrayQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self,value):
        if self.full():
            raise Exception("Queue is full")
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if not self.empty():
            return None
        value = self.queue[self.front]
        self.front = (self.front+1) % self.size
        self.count -= 1
        return value

    def empty(self):
        return self.count == 0

    def full(self):
        return self.count == self.size