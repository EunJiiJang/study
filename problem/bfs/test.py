from collections import deque

def bfs():
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        x = q.popleft()
        if dist[x] > t:
            break
        if x == g:
            print(dist[x])
            return
        dx = [(x+1), (x*2)]
        for i in range(2):
            nx = dx[i]
            if nx > 99999:
                continue
            if i and x:
                nx -= 10**(len(str(nx))-1)
            if dist[nx] == -1:
                q.append(nx)
                dist[nx] = dist[x]+1
    print("ANG")

n, t, g = map(int, input().split())
dist = [-1]*100000
bfs()


출처: https://rebas.kr/820 [PROJECT REBAS]