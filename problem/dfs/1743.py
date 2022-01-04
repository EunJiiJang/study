from collections import deque

def bfs(x,y):
    cnt = 0
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True

    while queue:
        x,y =queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1    # count food
    return cnt + 1


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n,m,k =map(int,input().split())
board = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]

for i in range(k):
    r,c = map(int,input().split())
    board[r-1][c-1] = 1

maxCnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] ==1 and not visit[i][j]:
            maxCnt = max(maxCnt,bfs(i,j))
print(maxCnt)