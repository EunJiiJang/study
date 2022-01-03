from itertools import combinations
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
mem = [i for i in range(n)]
po_team = []
for i in list(combinations(mem,n//2)):
    po_team.append(i)

min_gap =10000
#만들수 있는 팀중 절반만 두팀을 만들어야하기때문
for i in range(len(po_team)//2):
    team = po_team[i]
    abi_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            abi_A += lst[member][k]
    
    team = po_team[-i-1]
    abi_B = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            abi_B += lst[member][k]
    min_gap = min(min_gap, abs(abi_A - abi_B))

print(min_gap)