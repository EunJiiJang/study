n,k = map(int,input().split())

num = list(map(int,input()))
lst = []
delnum = k

for i in range(n):
    while delnum>0 and lst:
        if lst[len(lst)-1] <num[i]:
            lst.pop()
            delnum -= 1
        else:
            break
    lst.append(num[i])

for i in range(n-k):
    print(lst[i],end='')
