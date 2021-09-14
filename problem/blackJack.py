a,b = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))

result = 0
lenth = len(c)
for i in range(0,lenth):
    for j in range(i+1,lenth):
        for k in range (j+1,lenth):
            sum = c[i] + c[j] + c[k]
            if sum <= b:
                result = max(result,sum)
print(result)