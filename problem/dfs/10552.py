from collections import deque
n,m,p = map(int,input().split())
s = [[] for i in range(m+1)]
visit = [[] for i in range(m+1)]
for i in range(n):
    a,b = map(int,input().split())
    s[b].append(a)
    visit[b].append(0)

def dfs(start):
    q = deque()
    q.append(start)
    cnt = 0
    while q:
        st = q.popleft()
        for i in range(len(s[st])):
            if s[st][i] != 0 and visit[st][i] == 0:
                q.append(s[st][i])
                visit[st][i] = 1
                cnt += 1
                break
            if visit[st][i] == 1:
                return -1
    return cnt
print(dfs(p))