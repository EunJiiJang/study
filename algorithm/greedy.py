coinList = [1,100,50,500]


def min_coin_count(value,coinList):
    totalCoinCnt = 0
    details = list()
    coinList.sort(reverse=True)
    for coin in coinList:
        coinNum = value//coin
        totalCoinCnt += coinNum
        value -= coinNum*coin
        details.append([coin,coinNum])
    return totalCoinCnt,details

print(min_coin_count(4720,coinList))
