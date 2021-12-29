from itertools import permutations

n = int(input())
num = list(map(int,input().split(' ')))
plus = list(map(int,input().split(' ')))
items = []
ans = []
for i in range(4):
    for j in range(plus[i]):
        if i == 0:
            items.append('+')
        elif i == 1:
            items.append('-')
        elif i == 2:
            items.append('*')
        elif i == 3:
            items.append('//')
oper = list(set(permutations(items,len(items))))
for i in oper:
    n =num[0]
    for j in range(len(num)-1):
        if i[j]=='+':
            n += num[j+1]
        elif i[j]=='-':
            n -= num[j+1]
        elif i[j]=='*':
            n *= num[j+1]
        else:
            if n//num[j+1] <0:
                n = -(-n//num[j+1])
            else:
                n = n//num[j+1]
    ans.append(n)
print(max(ans))
print(min(ans))