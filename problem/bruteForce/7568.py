n = int(input())
lst = []
num = []
for i in range(n):
    lst.append(list(map(int,input().split(' '))))

for i in range(n):
    g =1
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            g = g + 1
    print(g,end=" ")