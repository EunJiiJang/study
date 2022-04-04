n,k = map(int,input().split())
arr = list(map(int,input().split()))

dp = [0]*n
lmax,ans = 0,0
tmp = 0
left, right = 0,0

while True:
    if tmp >= k:
        lmax = 0 if left ==0 else max(lmax,dp[left -1])
        dp[right-1] = max(dp[right-1],lmax+tmp-k)
        tmp -= arr[left]
        left += 1
    elif right == n:break
    else:
        tmp += arr[right]
        right += 1
for i in range(n):
    ans = max(ans,dp[i])
print(ans)