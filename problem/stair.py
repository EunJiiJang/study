n = int(input())

stair = []
dp = []
for _ in range(n):
    stair.append(int(input()))

if n==1: 
    print(stair[0]) 
    exit() 
elif n == 2:
    print(max(stair[0]+stair[1], stair[1])) 
    exit() 


dp.append(stair[0])
dp.append(max(dp[0]+stair[1],stair[1]))
dp.append(max(dp[0]+stair[2],stair[1]+stair[2]))
for i in range(3,n):
    dp.append(max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i]))

print(dp[-1])
exit()


