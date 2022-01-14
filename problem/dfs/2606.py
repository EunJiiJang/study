n = int(input())
m = int(input())
lst = [[]*n for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

cnt = 0
visit = [0]*(n+1)
def dfs(start):
  global cnt
  visit[start] = 1
  for i in lst[start]:
    if visit[i] == 0:
      dfs(i)
      cnt += 1
dfs(1)
print(cnt)