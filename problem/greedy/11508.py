n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse= True)
sum = sum(lst)
for i in range(n):
    if (i+1)%3 == 0:
        sum -= lst[i]

print(sum)