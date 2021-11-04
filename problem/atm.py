n = int(input())
a = list(map(int,input().split(' ')))

minimum = 0
a.sort()

for i in range (n):
    for j in range(i+1):
        minimum += a[j]

print(minimum)
