n = int(input())

for _ in range(n):
    a = int(input())
    lst = list(map(int,input().split()))
    sum = 0
    max = 0

    for i in range(len(lst)-1,-1,-1):
        if (lst[i]>max):
            max = lst[i]
        else:
            sum += max - lst[i]
    print(sum)