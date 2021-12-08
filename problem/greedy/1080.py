a,b = map(int,input().split())

g1 = []
g2 = []
cnt = 0

def covert(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            g1[x][y] = 1-g1[x][y]

for i in range(a):
    g1.append(list(map(int,input())))

for i in range(a):
    g2.append(list(map(int,input())))

for i in range(a-2):
    for j in range(b-2):
        if g1[i][j] != g2[i][j]:
            covert(i,j)
            cnt += 1

flag = 0
for i in range(a):
    for j in range(b):
        if g1[i][j] != g2[i][j]:
            flag = 1
            break

if flag == 1:
    print(-1)
else:
    print(cnt)