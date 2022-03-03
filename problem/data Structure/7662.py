import sys
input = sys.stdin.readline
from collections import deque

for i in range(int(input())):
    q =deque
    n = int(input())
    x = input()
    a = x[0]
    b = int(x[1])
    if a == 'I':
        q.append(b)
        
    elif a == 'D':
        if b == 1:
            q.pop()
        elif b== -1:
            q.popleft()

