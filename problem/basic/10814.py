n = int(input())
lst = []
for _ in range(n):
    data = input().split(' ')
    lst.append((int(data[0]),data[1]))

lst = sorted(lst,key=lambda x:x[0])
for i in lst:
    print(i[0],i[1])