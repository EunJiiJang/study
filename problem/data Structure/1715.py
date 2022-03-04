import heapq
import sys
input = sys.stdin.readline
n = int(input())
lst = []
res = 0
for i in range(n):
    lst.append(int(input()))
heapq.heapify(lst)
while len(lst) != 1:
    n1 = heapq.heappop(lst)
    n2 = heapq.heappop(lst)
    sum = n1 + n2
    res += sum
    heapq.heappush(lst,sum)

print(res)