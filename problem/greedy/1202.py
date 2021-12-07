import sys
import heapq
input = sys.stdin.readline
a,b = map(int,input().split())
bag = []
jew = []
sum = 0

for i in range(a):
     heapq.heappush(jew,list(map(int,input().split())))

for i in range(b):
    bag.append(int(input()))

bag.sort()
temp = []
for i in bag:
    while jew and i >= jew[0][0]:
        x,y =heapq.heappop(jew)
        heapq.heappush(temp,-y)
    if temp:
        sum -= heapq.heappop(temp)

print(sum)