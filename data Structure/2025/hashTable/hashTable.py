# Implement with array using linear probing
#
# hash(k, m) - m is the size of the hash table
# add(key, value) - if the key already exists, update value
# exists(key)
# get(key)
# remove(key)
class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None] * size
        self.DELETED = object()  # 삭제된 자리를 표시하는 특수 객체

    def hash(self,key):
        return hash(key) % self.size

    def add(self,key,value):
        idx = self.hash(key)
        org_idx = idx

        while self.table[idx] is not None and self.table[idx] is not self.DELETED:
            if isinstance(self.table[idx],tuple):
                k, _ = self.table[idx]
                if k == key:
                    self.table[idx] = (key,value) #update
                    return
            idx = (idx+1) % self.size
            if idx == org_idx:
                raise Exception("HashTable is full")
        self.table[idx] = (key,value)

    def exists(self, key):
        idx = self.hash(key)
        original_idx = idx

        while self.table[idx] is not None:
            if self.table[idx] is not self.DELETED:
                k, _ = self.table[idx]
                if k == key:
                    return True
            idx = (idx + 1) % self.size
            if idx == original_idx:
                break
        return False

    def get(self, key):
        idx = self.hash(key)
        original_idx = idx

        while self.table[idx] is not None:
            if self.table[idx] is not self.DELETED:
                k, v = self.table[idx]
                if k == key:
                    return v
            idx = (idx + 1) % self.size
            if idx == original_idx:
                break
        return None

    def remove(self, key):
        idx = self.hash(key)
        original_idx = idx

        while self.table[idx] is not None:
            if self.table[idx] is not self.DELETED:
                k, _ = self.table[idx]
                if k == key:
                    self.table[idx] = self.DELETED
                    return
            idx = (idx + 1) % self.size
            if idx == original_idx:
                break
