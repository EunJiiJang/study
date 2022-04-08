user = ["muzi", "frodo", "apeach", "neo"]
report =  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
report2 =  ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
rpt_list = {}
result = {}
report = set(report)
print(report)
for i in range(len(user)):
    for j in report:
        n,m = j.split()
        if user[i] == m:
            if user[i] in rpt_list:
                rpt_list[user[i]] += 1
            else:
                rpt_list[user[i]] = 1
        elif user[i] == n:
            if user[i] in result:
                result[user[i]] += 1
            else:
                result[user[i]] = 1

for n,m in rpt_list.items:
    if m <= k:
        result[n] = 0
val = result.values()
print(val)
