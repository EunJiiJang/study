n =int(input())

lst = []

for i in range(n):
    lst.append(int(input()))
cnt = 0
for i in range(len(lst)-1,0,-1):
    if lst[i] == lst[i-1]:
        lst[i-1] = lst[i-1]-1
        cnt += 1
    elif lst[i] < lst[i-1]:
        cnt += lst[i-1]-(lst[i]-1)
        lst[i-1] = lst[i-1]-(lst[i-1]-(lst[i]-1))

print(cnt)