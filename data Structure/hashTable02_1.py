#같은주소 저장 충돌해결 알고리즘
hash_table = list([0 for i in range(8)])

def getKey(data):
    return hash(data)

def hashFunc(key):
    return key%8

def saveData(data,value):
    indexKey = getKey(data)
    hashAddr = hashFunc(indexKey)
    if hash_table[hashAddr]  != 0:
        for index in range(len(hash_table[hashAddr])):
            if hash_table[hashAddr][index][0] == indexKey:
                hash_table[hashAddr][index][1] = value
                return
        hash_table[hashAddr].append([indexKey,value])
    else:
        hash_table[hashAddr] = [[indexKey,value]]
    

def readData(data):
    indexKey = getKey(data)
    hashAddr = hashFunc(getKey(data))
    if hash_table[hashAddr] != 0:
        for index in range(len(hash_table[hashAddr])):
            if hash_table[hashAddr][index][0] == indexKey:
                return hash_table[hashAddr][index][1]
        return None
    return hash_table[hashAddr]

print(hash('Dd')%8)
print(hash('Data')%8)

saveData("Dd",'010102')
saveData("Data",'010103')
print(readData('Dd'))


print(hash_table)
