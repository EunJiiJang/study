n = int(input())
#결과저장배열
dp = [0 for i in range(n+1)]
#모든 제곱수 <= 100000
sq = [i*i for i in range(1,317)]
for i in range(1,n+1):
    s = []
    for j in sq:
        if j > i:#제곱수가 기준수보다 클때
            break
        s.append(dp[i-j])
    dp[i]=min(s)+1
print(dp[n])