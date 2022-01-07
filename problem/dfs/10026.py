from collections import deque
n = int(input())
visit = [[False]*n for _ in range(n)]
board = [[]*n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    color = str(input())
    for x in color:
        board[i].append(x)

def bfs(x,y,color):
    q = deque()
    q.append((x,y))
    visit[x][y] =True

    while q:
       a,b = q.popleft()  

       for i in range(4):
           nx = a + dx[i]
           ny = b + dy[i]
           if 0<=nx<n and 0<=ny<n:
               if board[nx][ny] == color and not visit[nx][ny]:
                   visit[nx][ny] = True
                   q.append((nx,ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            color = board[i][j]
            bfs(i,j,color)
            cnt += 1

visit = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

cntColor = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            color = board[i][j]
            bfs(i,j,color)
            cntColor += 1

print(cnt)
print(cntColor)