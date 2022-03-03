import sys 
input = sys.stdin.readline
import heapq
n = int(input())
lst = []
for i in range(n):
    com = int(input())
    if com == 0:
        if len(lst)==0:
            print(0)
        else:
            print(-lst[0])
            heapq.heappop(lst)
    else:
        heapq.heappush(lst,-int(com))