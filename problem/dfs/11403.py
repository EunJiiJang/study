n = int(input())
visit = [0 for i in range(n)]
s = []

for i in range(n):
    s.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if s[j][i] == 1 and s[i][k] == 1:
                s[j][k] = 1
 
for i in s:
    print(*i)

def dfs(v):
    for i in range(n):
        if visited[i] == 0 and matrix[v][i] == 1:
            visited[i] = 1
            dfs(i)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    print(*visited)