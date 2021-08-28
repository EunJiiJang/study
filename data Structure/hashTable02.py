hash_table = list([0 for i in range(8)])

def getKey(data):
    return hash(data)

def hashFunc(key):
    return key%8

def saveData(data,value):
    hashAddr = hashFunc(getKey(data))
    hash_table[hashAddr] = value

def readData(data):
    hashAddr = hashFunc(getKey(data))
    return hash_table[hashAddr]

saveData("Dave",'010102')
saveData("Andy",'010103')
print(readData('Dave'))


