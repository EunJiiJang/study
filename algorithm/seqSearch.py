from random import*

randData = list()
for num in range(10):
    randData.append(randint(1,100))

def seqe(data_list,search_data):
    for idx in range(len(data_list)):
        if data_list[idx] == search_data:
            return idx
    return -1

print(seqe(randData,4))