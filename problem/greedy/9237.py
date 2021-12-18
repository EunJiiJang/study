n = int(input())

lst = list(map(int,input().split(' ')))
lst.sort(reverse=True)

for i in range(len(lst)):
   lst[i] = lst[i]+1+i
print(max(lst)+1)