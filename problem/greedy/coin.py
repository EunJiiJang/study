a ,b = map(int,input().split(' '))
coinList = []
coinCount = 0
for _ in range(a):
    coinList.append(int(input()))

coinList.sort(reverse=True)
for coin in coinList:
    coinNum = b//coin
    coinCount += coinNum
    b -= coinNum*coin

print(coinCount)
