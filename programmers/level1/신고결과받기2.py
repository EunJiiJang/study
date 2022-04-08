from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    to = defaultdict(set)
    from_to= defaultdict(set)
    for i in report:
        n,m = i.split(' ')
        to[m].add(n)
        from_to[n].add(m)
    for id in id_list:
        cnt = 0
        for r_to in from_to[id]:
            if len(to[r_to]) >= k:
                cnt+=1
        answer.append(cnt)


    return answer





id_list = ["muzi", "frodo", "apeach", "neo"]
report =  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

print(solution(id_list, report, k))