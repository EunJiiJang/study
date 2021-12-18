import sys

input = sys.stdin.readline
g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
plan =[]
answer = 0

for _ in range(p):
    plan.append(int(input()))


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


for plane in plan:
    docking = find(plane)
    if docking == 0:
        break
    parent[docking] = parent[docking - 1]
    answer += 1
print(answer)