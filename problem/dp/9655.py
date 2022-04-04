n = int(input())

n = int(input())
if n%2 == 0:
    print("CY")
else:
    print("SK")

##############################쓰레기 코드....

dp = [0 for i in range(n+1)]
dp[1] = 1
for i in range(1,n+1):
    if i == 1:
        if n > 3:
            dp[2] = 1
            dp[3] = 1
    if dp[i] == 0: 
        if (n+1)-i > 3:
            if dp[i-1] == 1:
                dp[i] = 2
                dp[i+1] = 2
                dp[i+2] = 2
            else:
                dp[i] = 1
                dp[i+1] = 1
                dp[i+2] = 1
        else:
            if dp[i-1] == 1:
                dp[i] = 2
            else:
                dp[i] = 1
                

if dp[n] == 1:
    print("SK")
else:
    print("CY")
