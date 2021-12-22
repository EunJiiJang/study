n = int(input())

cnt = 0

for i in range(1,n+1):
    if i<=99:
        cnt += 1
    else:
        lst = list(map(int,str(i)))
        if lst[0]-lst[1] == lst[1]-lst[2]:
            cnt += 1

print(cnt)