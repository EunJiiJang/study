a,b = map(int,input().split())

lst = list(map(int,input().split(' ')))
lst.sort()
cnt = 1
start = lst[0]
end = lst[0]+b


for i in range(a):
    if start <= lst[i] < end:
        continue
    else:
        start = lst[i]
        end = lst[i]+b
        cnt += 1

print(cnt)