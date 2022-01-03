from collections import deque
n = int(input())
lst = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
max = 0
for i in range(n):
    lst.append(list(map(int,input().split(' '))))
    for j in range(n):
        if lst[i][j] > max:
            max = lst[i][j]
rst = []

def bfs(xPos, yPos, value, visit):
    q = deque()
    q.append((xPos, yPos))
    visit[xPos][yPos] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] > value and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))

maximum = 0
for i in range(max):
    visit = [[0] * n for _ in range(n)]
    ans = 0
    for j in range(n):
        for k in range(n):
            if lst[j][k] > i and visit[j][k] == 0:
                bfs(j,k,i,visit)
                ans +=1
    if maximum < ans:
        maximum = ans