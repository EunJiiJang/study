import sys
input = sys.stdin.readline##시간초과,메모리초과 해결요인
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[]for i in range(n+1)]

parent = [0 for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(parent[i])