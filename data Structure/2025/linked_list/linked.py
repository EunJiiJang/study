# 목록에 있는 데이터 요소의 수를 반환합니다.
# empty() - bool은 비어 있으면 true를 반환합니다.
# value_at(index) - n번째 항목의 값을 반환합니다(첫 번째 항목은 0부터 시작)
# push_front(값) - 목록의 앞에 항목을 추가합니다.
# pop_front() - 앞쪽 항목을 제거하고 해당 값을 반환합니다.
# push_back(value) - 마지막에 항목을 추가합니다.
# pop_back() - 최종 항목을 제거하고 해당 값을 반환합니다.
# front() - 앞 항목의 값을 가져옵니다
# back() - 최종 항목의 값을 가져옵니다.
# insert(index, value) - index에 값을 삽입하므로 해당 index에 있는 현재 항목은 index에 있는 새 항목에 의해 가리켜집니다.
# erase(index) - 주어진 인덱스에서 노드를 제거합니다.
# value_n_from_end(n) - 리스트의 끝에서 n번째 위치에 있는 노드의 값을 반환합니다.
# reverse() - 목록을 뒤집습니다
# remove_value(value) - 이 값을 가진 목록의 첫 번째 항목을 제거합니다.
from node import Node

class LinkedList(object):
    def __init__(self):
        self.head_ = None

    def set_head(self, head_node):
        self.head_ = head_node

    def __len__(self):
        cnt = 0
        current = self.head_
        while current:
            cnt += 1
            current = current.next
        return cnt

    def empty(self):
        return self.head_ is None

    def value_at(self,index):
        current = self.head_
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
        if self.head_ is None:#리스트 존재여부 확인
            raise IndexError("Pop from empty list")
        value = self.head_.value#pop해서 해당 노드지우기전에 값 빼기
        self.head_ = self.head_.next#가장앞의 헤드를 다음 요소로 바꾸면됨
        return value

    def push_back(self, value):
        new_node = Node(value)#맨 뒤로 넣을 노드 선언
        if self.head_ is None:
            self.head_ = new_node#리스트가 존재하지않는다면 헤드가 되고 리턴
            return
        current = self.head_#반복문 시작점 선언
        while current.next:
            current = current.next#끝까지 돌아서 다음요소가 없는 마지막 노드 찾기
        current.next = new_node#마지막요소 다음에 값넣기

    def front(self):
        if self.head_ is None:
            raise IndexError("Empty list")
        return self.head_.value

    def back(self):
        if self.head_ is None:
            raise IndexError("Empty list")
        current = self.head_
        while current.next:
            current = current.next
        return current.value
    # 앞선 클래스 정의에 이어서 아래 메서드들을 추가하면 됩니다.

    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
            return
        new_node = Node(value)
        current = self.head_
        for _ in range(index - 1):#내가 찾는 인덱스직전요소까지 돌린다름 새로넣을 요소 다음요소를 현재요소로 넣고
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node#현재요소의 다음요소를 새로운노드로 넣기

    def erase(self, index):
        if self.head_ is None:
            raise IndexError("Erase from empty list")
        if index == 0:
            self.head_ = self.head_.next
            return
        current = self.head_
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current.next is None:
            raise IndexError("Index out of bounds")
        current.next = current.next.next

    def value_n_from_end(self, n):#???
        slow = self.head_
        fast = self.head_
        for _ in range(n):
            if fast is None:
                raise IndexError("Index out of bounds")
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow is None:
            raise IndexError("Index out of bounds")
        return slow.value

    def reverse(self):
        prev = None
        current = self.head_
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head_ = prev

    def remove_value(self, value):
        if self.head_ is None:
            return
        if self.head_.value == value:
            self.head_ = self.head_.next
            return
        current = self.head_
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

