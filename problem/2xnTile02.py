###
n = int(input())

num = [0,1,3]

for i in range(3,n+1):
    num.append(num[i-1]+(2*num[i-2]))
print(num[n]%10007)