from collections import deque
from random import random
import re
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
s = []
t = deque()
dy = [0,0,-1,1]
dx = [1,-1,0,0]
for i in range(n):
    s.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            t.append([i,j])

def bfs():
    while t:
        a,b = t.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<= x <n and 0<=y<m and s[x][y] ==0:
                s[x][y] = s[a][b]+1
                t.append([x,y])
bfs()
isTrue = False
result = -2
for i in s:
    for j in i:
        if j == 0:
            isTrue =True
        result = max(result,j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result -1)
