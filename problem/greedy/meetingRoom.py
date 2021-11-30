n = int(input())
arr = []
for _ in range(n):
    data = input().split(' ')
    arr.append((int(data[0]),int(data[1])))

arr.sort(key=lambda x:(x[1], x[0]))
cnt = 1
endTime = arr[0][1]
for i in range(1,n):
    if arr[i][0] >= endTime:
        cnt += 1
        endTime = arr[i][1]
print(cnt)