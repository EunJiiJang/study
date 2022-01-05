from collections import deque
n = int(input())
board = [[0] * n for _ in range(n)]
visit = [[False] * n for _ in range(n)]

#
def bfs(x,y):
    cnt = 0
    q = deque()
    q.append((x,y))
    visit[x][y] = True

    while q:
        x,y =q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt + 1
  

#
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    lst = list(map(int,input()))
    for j,b in enumerate(lst):
        board[i][j] = int(b)

vitCnt = 0
result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visit[i][j]:
            vitCnt = bfs(i,j)
            result.append(vitCnt)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

