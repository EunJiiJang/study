lst = [ ]
ans = [0]*1001

for i in range(1,46):
    lst.append(i*(i+1)//2)

for i in lst:
    for j in lst:
        for k in lst:
            if i+j+k <= 1000:
                ans[i+j+k] = 1

n = int(input())
for i in range(n):
    print(ans[int(input())])

