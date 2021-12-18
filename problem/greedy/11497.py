t = int(input())

for i in range(t):
    n =int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    rst = 0
    for j in range(2,n):
        rst = max(rst,abs(tree[j]-tree[j-2]))
    print(rst)
    
