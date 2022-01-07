import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
maxCnt = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(y,x):
    if t[y][x] > k:
        t[y][x] = k
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                dfs(ny,nx)


for k in range(1,max(map(max,board))+1):
    t = deepcopy(board)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if t[i][j] > k:
                dfs(i,j)
                cnt += 1
    maxCnt = max(cnt,maxCnt) 
print(maxCnt)