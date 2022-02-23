import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    cnt = 0
    lst = input()
    for j in lst:
        if j == "(":
            cnt += 1
        elif j == ")":
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
        
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
