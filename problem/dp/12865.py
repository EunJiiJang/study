n,k = map(int,input().split())
dp = [[0]*(k+1) for i in range(n+1)]
thing = [[0,0]]#1번째부터 카운팅위해 삽입
for i in range(n):
    thing.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[n][k])