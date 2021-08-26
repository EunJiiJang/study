hash_table = list([i for i in range(10)])

print(hash_table)

def hash_func(key):
    return key%5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

#ord(): 문자의 아스키 코드리턴
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
print(hash_func(ord(data1[0])),ord(data2[0]),ord(data3[0]))

def strg_data(data,value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

strg_data(data1,'1010')

strg_data(data2,'11010')

strg_data(data3,'21010')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))