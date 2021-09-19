u = int(input())

arr = [0,1,1,2]

lenth = len(arr)
if u >= lenth:
    for i  in range(lenth,u+1):
        arr.append(arr[i-1]+arr[i-2])
            
print(arr[u])
