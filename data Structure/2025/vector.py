import ctypes

class Vector:
    def __init__(self):
        self._capacity = 16
        self._size = 0
        self._array = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._size == 0

    def at(self, index):
        if not 0 <= index < self._size:
            raise IndexError('Index out of bounds')
        return self._array[index]

    def push(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._array[self._size] = item
        self._size += 1

    def insert(self, index, item):
        if not 0 <= index <= self._size:
            raise IndexError('Index out of bounds')
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = item
        self._size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self._size == 0:
            raise IndexError('Pop from empty vector')
        item = self._array[self._size - 1]
        self._size -= 1
        if 0 < self._size < self._capacity // 4:
            self._resize(max(self._capacity // 2, 16))
        return item

    def delete(self, index):
        if not 0 <= index < self._size:
            raise IndexError('Index out of bounds')
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
        if 0 < self._size < self._capacity // 4:
            self._resize(max(self._capacity // 2, 16))

    def remove(self, item):
        i = 0
        while i < self._size:
            if self._array[i] == item:
                self.delete(i)
            else:
                i += 1

    def find(self, item):
        for i in range(self._size):
            if self._array[i] == item:
                return i
        return -1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
