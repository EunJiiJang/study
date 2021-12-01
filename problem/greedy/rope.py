n = int(input())
list = []
sum = []
for i in range(n):
    list.append(int(input()))

list.sort(reverse=True)
for i in range(n):
    sum.append(list[i]*(i+1))

print(max(sum))
