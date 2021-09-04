import random
def insertSort(data):
    for idx in range(len(data)-1):
        for idx2 in range(idx + 1, 0, -1):
            if data[idx2] < data[idx2-1]:
                data[idx2],data[idx2 - 1]=data[idx2-1],data[idx2]
            else:
                break
    return data
data_list = random.sample(range(100),10)
print(data_list)
print(insertSort(data_list))