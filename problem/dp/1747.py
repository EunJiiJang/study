n = int(input())

l = [0]*1003002
l[1]=[1]

for i in range(2,n):
    if l[i] == 0:
        for j in range(i,1003002,i):
            l[j] = 1

for i in range(n,1003002):
    if l[i] == 0:
        if str(i) ==str(i)[::-1]:
            print(i)
            break
        else:
            for k in range(i,1003002,i):
                l[k] = 1