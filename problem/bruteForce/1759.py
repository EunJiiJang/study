from itertools import combinations
n,m = map(int,input().split(' '))
lst = list(input().split(' '))
lst.sort()
rst = list(combinations(lst,n))
moum = ['a', 'e', 'i', 'o', 'u']

for c in rst:
    cnt = 0
    for let in c:
        if let in moum:
            cnt +=1
    if(cnt >= 1)and(cnt <= n-2):
        print(''.join(c))