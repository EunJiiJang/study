import random
def selecttionSort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for idx in range(stand+1,len(data)):
            if data[lowest] > data[idx]:
                lowest = idx
        data[lowest],data[stand] = data[stand],data[lowest]
    return data

data_list = random.sample(range(100),10)
print(data_list)
print(selecttionSort(data_list))