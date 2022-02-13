from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([a,""])
    while q:
        num,result = q.popleft()
        dn = (num*2)%10000
        if dn == b:
            return result+"D"
        elif arr[dn] == 0:
            arr[dn] = 1
            q.append([dn,result+"D"])
        sn = num - 1 if num != 0 else 9999
        if sn == b :
            return result+"S"
        elif arr[sn] == 0:
            arr[sn] = 1
            q.append([sn,result+"S"])
        ln = int(num %1000*10+num/1000)
        if ln == b:
            return result+"L"
        elif arr[ln] == 0:
            arr[ln] = 1
            q.append([ln,result+"L"])
        rn = int(num%10*1000+num//10)
        if rn == b:
            return result+"R"
        elif arr[rn] == 0:
            arr[rn] = 1
            q.append([rn,result+"R"])
        
        

t = int(input())
for i in range(t):
    a,b =map(int,input().split())
    arr = [0 for i in range(10000)]
    print(bfs())