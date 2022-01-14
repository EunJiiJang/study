import sys

sys.setrecursionlimit(10 ** 7)
t = int(input())

def dfs(n):
    global result
    visit[n] = 1
    team.append(n)
    num = board[n]

    if(visit[num]):
        if num in team:
            result += team[team.index(num):]
        return
    else:
        dfs(num)


for _ in range(t):
    n = int(input())
    board =[0] + list(map(int,input().split()))
    visit = [0] * (n+1)
    result = []
    for i in range(1,n+1):
        if visit[i] == 0:
            team = []
            dfs(i)
    print(n-len(result))