import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v,group):
    visit[v] = group
    for i in board[v]:
        if visit[i] == 0:
            if not dfs(i,-group):
                return False
        elif visit[i] == visit[v]:
            return False
    return True

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    board = [[]for i in range(v+1)]
    visit = [0]*(v+1)

    for _ in range(e):
        a,b = map(int,input().split())
        board[a].append(b)
        board[b].append(a)
    bipatite = True

    for i in range(1,v+1):
        if visit[i] == 0:
            bipatite = dfs(i,1)
            if not bipatite:
                break
    print('YES' if bipatite else 'NO')