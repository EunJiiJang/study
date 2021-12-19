n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()
rst = 0
for i in range(1,n+1):
    rst +=abs(i-lst[i-1])

print(rst)