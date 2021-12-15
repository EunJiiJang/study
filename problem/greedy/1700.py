#????
a,b = map(int,input().split())

multitap = list(map(int,input().split()))
cnt = 0
plugs = []

for i in range(b):
    if multitap[i] in plugs:
        continue
    if len(plugs) < a:
        plugs.append(multitap[i])
        continue

    idx = []
    hashp = True

    for j in range(a):
        if plugs[j] in multitap[i:]:
            idx_temp = multitap[i:].index(plugs[j])
        else:
            idx_temp = 101
            hasplug = False

        idx.append(idx_temp)
        if not hashp:
            break

    plug_out = idx.index(max(idx))
    del plugs[plug_out] # 플러그에서 제거
    plugs.append(multitap[i]) # 플러그에 멀티탭 값 삽입
    cnt += 1 # 뽑았으므로 1 증가
        
print(cnt)
