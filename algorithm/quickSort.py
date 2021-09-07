def qSort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left, right= list(),list()

    for n in range(1,len(data)):
        if pivot > data[n]:
            left.append(data[n])
        else:
            right.append(data[n])

    return qSort(left) + [pivot] + qSort(right)

import random

dataList = random.sample(range(100),10)
print(qSort(dataList))



##간결한 코드
def qSort_S(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qSort_S(left) + [pivot] + qSort_S(right)

dataList = random.sample(range(100),10)
print(qSort_S(dataList))