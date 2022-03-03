import heapq
import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    x = list(map(int,input().split()))

    if not lst:
        for y in x:
           heapq.heappush(lst,y) 
    else:
        for y in x:
            if lst[0] <y:
                heapq.heappush(lst,y)
                heapq.heappop(lst)


print(lst)
print(lst[0])