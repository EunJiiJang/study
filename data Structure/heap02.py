class Heap:
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self,inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array)-1
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx],self.heap_array[parent_idx] = self.heap_array[parent_idx],self.heap_array[inserted_idx]
            inserted_idx = parent_idx

            


        return True

    def move_down(self,poped_idx):
        left_child_poped_idx =poped_idx * 2
        right_child_poped_idx = poped_idx * 2 + 1

        #case1:왼쪽 자식 노드도 없을때
        if left_child_poped_idx >=  len(self.heap_array):
            return False
            
        #case2:오른쪽 자식 노드만 없을때
        elif right_child_poped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                return True
            else:
                return False
        #case3:왼쪽,오른쪽 자식 노드모두 있을때
        else:
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        poped_idx = 1

        while self.move_down(poped_idx):
            left_child_poped_idx =poped_idx * 2
            right_child_poped_idx = poped_idx * 2 + 1

            #case2:오른쪽 자식 노드만 없을때
            if right_child_poped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    self.heap_array[poped_idx],self.heap_array[left_child_poped_idx]=self.heap_array[left_child_poped_idx],self.heap_array[poped_idx]
                    poped_idx = left_child_poped_idx
            
            #case3:왼쪽,오른쪽 자식 노드모두 있을때
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                        self.heap_array[poped_idx],self.heap_array[left_child_poped_idx]=self.heap_array[left_child_poped_idx],self.heap_array[poped_idx]
                        poped_idx = left_child_poped_idx
                    
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                        self.heap_array[poped_idx],self.heap_array[right_child_poped_idx]=self.heap_array[right_child_poped_idx],self.heap_array[poped_idx]
                        poped_idx = right_child_poped_idx
                    

        return returned_data
    
    

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

print(heap.pop())