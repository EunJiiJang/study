time = [300,60,10]
n = int(input())
details = []
for i in time:
    num = n//i
    n -= i*num
    details.append(num)


if n != 0:
    print(-1)
else:
    for i in details:
        print(i,end=' ')