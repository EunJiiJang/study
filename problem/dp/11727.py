n = int(input())
lst = [0,1,3]
for i in range(3,n+1):
    lst.append((2*lst[i-2])+lst[i-1])

print(lst[n]%10007)