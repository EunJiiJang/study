from  collections import deque
import copy

def bfs():
    q = deque()
    temp = copy.deepcopy(lst)
    for i in range(n):
        for j  in range(m):
            if temp[i][j] == 2:
                q.append((i,j))

    while q:
        x,y =q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))
    global answer
    cnt = 0

    for i in range(n):
        cnt += temp[i].count(0)
    answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wall(cnt+1)
                lst[i][j] = 0
                
n,m = map(int,input().split(' '))
lst = []
for i in range(n):
    lst.append(list(map(int,input().split(' '))))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


answer = 0
wall(0)
print(answer)
