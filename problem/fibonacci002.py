###
n = int(input())

arr = [0,1,1,2]

for i in range (len(arr),n+1):
    arr.append(arr[i-1]+arr[i-2])

print(arr[n])