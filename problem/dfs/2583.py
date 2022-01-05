from collections import deque
m,n,k =map(int,input().split())
board = [[0]*n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(k):
    a,b,c,d =map(int,input().split())
    for x in range(a,c):
        for y in range(b,d):
            board[y][x] = -1

result = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            cnt = 1
            q = deque()
            q.append([i,j])
            board[i][j] = cnt
            
            while q:
                y,x =q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and board[ny][nx] == 0:
                        board[ny][nx] = 1
                        q.append([ny,nx])
                        cnt += 1
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i,end=" ")