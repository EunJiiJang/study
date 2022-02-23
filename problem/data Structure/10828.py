import sys
input = sys.stdin.readline
n = int(input())
lst = list()
for i in range(n):
    p = input().split()
    a = p[0]
    if a =="push":
        b =p[1]
    
    if a == "push":
        lst.append(int(b))
    elif a == "pop":
        if len(lst) > 0:
            x = lst.pop()
            print(x)
        else:
            print(-1)
    elif a == "size":
        print(len(lst))
    elif a == "empty":
       print(0) if len(lst)>0 else print(1)
    elif a == "top":
        if len(lst) > 0:
            print(lst[-1])
        else:
            print(-1)