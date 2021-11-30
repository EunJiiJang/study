n = int(input())

tList = []
for _ in range(n):
    tList.append(list(map(int,input().split())))

#7은 건너띄고 시작
for i in range(1,n):
    for j in range(len(tList[i])):
            if j == 0:
                tList[i][j] = tList[i][j] + tList[i-1][j]
            elif i == j:
                tList[i][j] = tList[i][j] + tList[i-1][j-1]
            else:
                tList[i][j] = max(tList[i][j]+tList[i-1][j-1],
                                    tList[i][j]+tList[i-1][j])

print(max(tList[-1]))