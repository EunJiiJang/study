import sys
input = sys.stdin.readline
import heapq

k,n =map(int,input().split())
num = list(map(int,input().split()))
lst = list(num)
heapq.heapify(lst)
h = None
for _ in range(n):
    h =heapq.heappop(lst)
    for a in num:
        heapq.heappush(lst,h*a)
        if(h % a == 0):
            break
print(h)
