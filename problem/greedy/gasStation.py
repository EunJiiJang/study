n = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))
#결과값
res = 0
m = cost[0]

for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    res += m*road[i]

print(res)

# m에 첫번째 도시 코스트 선언
# 반복 시작
# 도시의 코스트가 m보다 작을 경우 m을 그 도시의 코스트로 선언
# 다음도시로 향하기 위한 거리*m
# m보다 크면 이전도시 코스트가 담긴 m*다음도시로 향하기 위한 거리