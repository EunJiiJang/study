import heapq
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
heapq.heapify(lst)
rst = 0

while len(lst) != 1:
    n1 = heapq.heappop(lst)
    n2 = heapq.heappop(lst)
    sum = n1 + n2
    rst += sum
    heapq.heappush(lst,sum)

print(rst)