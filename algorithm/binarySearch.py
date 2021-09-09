def binarySearch(data,search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data)//2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binarySearch(data[medium:],search)
        else:
            return binarySearch(data[:medium],search)

import random
data_list = random.sample(range(100),10)
data_list.sort()
print(data_list)
print(binarySearch(data_list,92))
        