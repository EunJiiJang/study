import sys
input = sys.stdin.readline
n,m = map(int,input().split())

poc = {}

for i in range(1,n+1):
    name = input().strip()
    poc[i] = name
    poc[name] = i

for i in range(m):
    x = input().strip()
    if x.isdigit():
        print(poc[int(x)])
    else:
        print(poc[x])
