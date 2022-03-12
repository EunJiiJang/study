n = int(input())
lst = [0,1,2]
for i in range(3,n+1):
    lst.append(lst[i-2]+lst[i-1])

print(lst[n]%10007)