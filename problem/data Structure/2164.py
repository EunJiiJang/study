from collections import deque
n = int(input())

lst = deque()
for i in range(1,n+1):
    lst.append(i)

for i in range(n):
    
    if len(lst)==1:
        x = lst.pop()
        print(x)
    else:
        lst.popleft()
        x = lst.popleft()
        lst.append(x)
