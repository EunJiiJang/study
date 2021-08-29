import hashlib

data = 'test'.encode
hashOb = hashlib.sha1()
hashOb.update(b'test')
hex_dig = hashOb.hexdigest()
#print(hex_dig)

hashOb = hashlib.sha256()
hashOb.update(b'test')
hex_dig = hashOb.hexdigest()
#print(hex_dig)


#sha256
#
hash_table = list([0 for i in range(8)])

def getKey(data):
    hashOb = hashlib.sha256()
    hashOb.update(data.encode())
    hex_dig = hashOb.hexdigest()
    return int(hex_dig,16)

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

print(getKey('db')%8)
print(getKey('da')%8)
print(getKey('dh')%8)

saveData("da",'010102')
saveData("dh",'010103')
print(readData('dh'))


# print(hash_table)
