from collections import deque
n = int(input())
board = [[0]*n for _ in range(n)]
visit = [[False]*n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    cnt = 0
    q = deque()
    visit[x][y] = True

    while q:
        a,b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
#보드에 1값 매칭하기
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visit[i][j]:
            bfs(i,j)
            