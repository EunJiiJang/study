import heapq
n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort()
room = []
heapq.heappush(room,arr[0][1])

for i in range(1,n):
    if arr[i][0]<room[0]:
        heapq.heappush(room,arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,arr[i][1])

print(len(room))
