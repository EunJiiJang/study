N, M = map(int, input().split())
cardnum = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cardnum[i] + cardnum[j] + cardnum[k] > M:
                continue
            else:
                result = max(result, cardnum[i] + cardnum[j] + cardnum[k])
print(result)