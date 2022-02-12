from collections import deque

def bfs():
    q = deque()
    q.append(n)
    visit[n] = 0
    while q:
        x = q.popleft()
        if visit[x] > t:
            break
        if x == g:
            print(visit[x])
            return
        dx = [(x+1), (x*2)]
        for i in range(2):
            nx = dx[i]
            if nx > 99999:
                continue
            if i and x:
                nx -= 10**(len(str(nx))-1)
            if visit[nx] == -1:
                q.append(nx)
                visit[nx] = visit[x]+1
    print("ANG")

n, t, g = map(int, input().split())
visit = [-1]*100000
bfs()

