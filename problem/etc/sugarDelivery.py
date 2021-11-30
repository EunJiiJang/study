value = int(input())

totalCnt = 0
while value >= 0:
    if value % 5 == 0:
        totalCnt += (value//5)
        print(totalCnt)
        break
    value -= 3
    totalCnt += 1
else:
    print(-1)
        
