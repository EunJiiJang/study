import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visit[v] = True
    for i in adj[v]:
        if not visit[i]:
            dfs(i)

n,m =map(int,input().split())
adj = [[] for _ in range(n+1)]
visit = [False] * (n + 1)
cnt = 0
for _ in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1,n+1):
    if not visit[j]:
        dfs(j)
        cnt += 1

print(cnt)