import sys
input = sys.stdin.readline
import heapq

n = int(input())
lst = []
for i in range(n):
    x = int(input())
    if x == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst)[1])
            
    else:
        heapq.heappush(lst,(abs(x),x))