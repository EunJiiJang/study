n = int(input())
coin = [25,10,5,1]
lst = []
for i in range(n):
    lst.append(int(input()))
for i in lst:
    coinList =[]
    num = 0
    for j in coin:
        num = i//j
        i -= num*j
        coinList.append([j,num])
    for x in range(4):
        print(coinList[x][1],end=' ')

    print()



