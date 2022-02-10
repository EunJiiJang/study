from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global q,w
    while q:
        temp = deque()
        while q:
            x,y = q.popleft()
            if (x == goal[0][0] and y == goal[0][1]) and s[x][y] != "*": 
                return s[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #이동했을때 불이없는곳
                if 0 <= nx < c and 0 <= ny < r and s[nx][ny] == "." and s[x][y] != "*":
                    s[nx][ny] = s[x][y] + 1
                    #새로이동한 곳에대해 조사필요
                    temp.append([nx, ny])
        q = temp
        temp = deque()
        while w:
            x, y = w.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < c and 0 <= ny < r and visit[nx][ny] == 0:
                    s[nx][ny] = "*"
                    visit[nx][ny] = 1
                    temp.append([nx, ny])
        w = temp


r,c = map(int,input().split())
s,q,w = [],deque(),deque()
visit = [[0]*c for i in range(r)]
goal = []
for i in range(r):
    s.append(list(input().strip()))
    for j in range(c):
        if s[i][j] == "S":
            q.append([i,j])
            s[i][j] = 0
        elif s[i][j] == "*":
            w.append([i,j])
            visit[i][j] = 1
        elif s[i][j] == "D":
            goal.append([i,j])
result = bfs()
print(result if result != None else "KAKTUS")