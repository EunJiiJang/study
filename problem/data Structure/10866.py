from collections import deque
import sys
input = sys.stdin.readline
lst = deque() 
for i in range(int(input())):
    p = input().split()
    a = p[0]
    if a == "push_back":
        lst.append(p[1])        
    elif a == "push_front":
        lst.appendleft(p[1])
    elif a == "pop_front":
        if len(lst) > 0:
            x = lst.popleft()
            print(x)
        else:
            print(-1)
    elif a == "pop_back":
        if len(lst) > 0:
            x = lst.pop()
            print(x)
        else:
            print(-1)
    elif a == "size":
        print(len(lst))
    elif a == "empty":
        print(0) if len(lst)>0 else print(1)
    elif a == "front":
        if len(lst) > 0:
            print(lst[0])
        else:
            print(-1)
    elif a == "back":
        if len(lst) > 0:
            print(lst[-1])
        else:
            print(-1)

