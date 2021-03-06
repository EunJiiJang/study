from collections import deque
n,k = map(int,input().split())
visit = [0 for i in range(100001)]
q = deque()
q.append([n,0])
while q:
    p,d = q[0][0],q[0][1]
    if p == k:
        break
    q.popleft()
    visit[p] = 1
    if p - 1>= 0 and visit[p-1]==0:
        q.append([p-1,d+1])
    if p+1<= 100000 and visit[p+1] == 0:
        q.append([p+1,d+1])
    if p*2 <=100000 and visit[p*2]==0:
        q.append([p*2,d+1])
print(q[0][1])