###
n = int(input())

arr = [1,1,1,2,2]

for i in range(5,100):
    arr.append(arr[i-1]+arr[i-5])

for _ in range(n):
    n = int(input())
    print(arr[n-1])


