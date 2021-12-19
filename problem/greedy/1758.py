n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
sum = 0
for i in range(n):
    if lst[i]-(i)>0:
        sum += lst[i]-(i)

print(sum)