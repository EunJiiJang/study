from collections import deque
n,t,g = map(int,input().split())
visit = [0 for i in range(100000)]

def bfs():
    q = deque()
    q.append(n)
    visit[n] = 1
    while q:
        x = q.popleft()
        if visit[x] > t:
            break
        if x == g:
            print(visit[x])
            break
        dx = [(x+1),(x*2)]
        for i in range(2):
            nx = dx[i]        
        if nx>99999:
            continue
        if i and x:
            nx -= 10**(len(str(nx))-1)
        if visit[nx] == 0:
            q.append(nx)
            visit[nx] = visit[x]+1
    print("ANG")
bfs()


