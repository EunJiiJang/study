u = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(n):
    lenth = len(zero)
    if n >= lenth:
        for i  in range(lenth,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[n],one[n]))

for i in range(u):
    a = int(input())
    fibo(a)

