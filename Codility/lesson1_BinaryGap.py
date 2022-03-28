def solution(N):
    binary = bin(N).lstrip('0b')
    cnt = 0
    maxc = 0
    for i in binary:
        if i=='1':
            if maxc < cnt :
                maxc = cnt
            cnt = 0
        else:
            cnt += 1
    return maxc