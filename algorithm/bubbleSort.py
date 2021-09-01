import random
def bubbleSort(data):
    for idx in range(len(data)-1):
        swap = False
        for idx2 in range(len(data)-idx-1):
            if data[idx2] > data[idx2+1]:
                data[idx2],data[idx2 + 1] = data[idx2 + 1],data[idx2]
                swap = True

        if swap == False:
            break
    return data

data_list = random.sample(range(100),50)
print(data_list)
print(bubbleSort(data_list))


