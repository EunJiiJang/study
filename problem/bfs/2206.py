import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append([0,0,1])
    visit = [[[0]*2 for i in range(m)]for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a,b,w = q.popleft()
        if a == n-1 and b == m-1:
            print(visit)
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x,y,0])
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1

n,m = map(int,input().split())
dx = [0,0,1,-1]
dy = [-1,1,0,0]
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())
