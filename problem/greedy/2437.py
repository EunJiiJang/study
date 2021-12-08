n = int(input())

lst = list(map(int,input().split()))
lst.sort()

cnt = 0
for i in  range(n):
    if cnt+1 >= lst[i]:
        cnt += lst[i]
    else:
        break

print(cnt+1)