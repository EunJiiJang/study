n = int(input())
cnt = 0
for i in range(1,n+1):
    lst = list(map(int,str(i)))
    cnt = i+sum(lst)
    if cnt == n:
        print(i)
        break
    if i == n:
        print(0)