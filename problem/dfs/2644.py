import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

def dfs(node):
    for i in board[node]:
        if chk[i] == 0:
            chk[i] = chk[node] + 1
            dfs(i)

n = int(input())
a,b = map(int,input().split())
#서로 관여되어있는 촌수를 표시
board = [[] for _ in range(n+1)]
for i in range(int(input())):
    u,v = map(int,input().split())
    board[u].append(v)
    board[v].append(u)
chk = [0]*(n+1)
dfs(a)
print(chk[b] if chk[b]>0 else -1)