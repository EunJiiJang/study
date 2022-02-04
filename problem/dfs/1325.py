from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in s[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt


n,m = map(int,input().split())
s = [[] for i in range(n+1)]
lst = []
for i in range(m):
    a,b =map(int,input().split())
    s[b].append(a)
result = []
maxCnt = 0
for i in range(1,n+1):
    tmp = bfs(i)
    if maxCnt == tmp:
        result.append(i)
    if maxCnt < tmp:
        maxCnt = tmp
        result = []
        result.append(i)
    
print(*result)