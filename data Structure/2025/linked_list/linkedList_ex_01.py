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

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node1.next = node2

cnt = 0
current = node1

while current:
    cnt += 1
    current = current.next

print(cnt)