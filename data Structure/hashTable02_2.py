#같은주소 저장 충돌해결 알고리즘
#
hash_table = list([0 for i in range(8)])

def getKey(data):
    return hash(data)

def hashFunc(key):
    return key%8

def saveData(data,value):
    indexKey = getKey(data)
    hashAddr = hashFunc(indexKey)
    if hash_table[hashAddr]  != 0:
        for index in range(hashAddr,len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [indexKey,value] 
                return
            elif hash_table[index][0] == indexKey:
                hash_table[index][1] = value
                return
    else:
        hash_table[hashAddr] = [indexKey,value]
    

def readData(data):
    indexKey = getKey(data)
    hashAddr = hashFunc(getKey(data))

    if hash_table[hashAddr] !=0:
        for index in range(hashAddr,len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index] == indexKey:
                return hash_table[index][1]
    else:
        return None


print(hash('Dd')%8)
print(hash('Data')%8)

saveData("Dd",'010102')
saveData("Data",'010103')
print(readData('Data'))


print(hash_table)
