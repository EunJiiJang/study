import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node):
    for i in s[node]:
        if visit[i] == 0:
            visit[i] = visit[node]+1
            dfs(i)

n = int(input())
a,b = map(int,input().split())
m = int(input())

s = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    u,v = map(int,input().split())
    s[u].append(v)
    s[v].append(u)

dfs(a)
print(visit[b] if visit[b]>0 else -1)
print(s)
print(visit)