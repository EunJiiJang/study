from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx,sy,ax,ay):
    q =deque()
    q.append([sx,sy])
    s[sx][sy] = 1
    while q:
        a,b = q.popleft()
        if a == ax and b == ay:
            print(s[ax][ay]-1)
            return
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0 <=x<l and 0<= y < l and s[x][y] == 0:
                q.append([x,y])
                s[x][y] = s[a][b]+1


t = int(input())
for i in range(t):
    l = int(input())
    s = [[0]*l for i in range(l)]
    sx,sy = map(int,input().split())
    ax,ay = map(int,input().split())
    bfs(sx,sy,ax,ay)