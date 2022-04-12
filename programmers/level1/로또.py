from collections import defaultdict

def solution(lottos, win_nums):
    answer = [0,0]
    s = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt = 0
    z = 0
    for i in lottos:
        if i == 0:
            z += 1
        elif i in win_nums:
            cnt += 1
    answer[0] = s[z+cnt]     
    answer[1] = s[cnt]

    return answer  





lottos = [44, 1, 0, 0, 31, 25]
win_nums =  [31, 10, 45, 1, 6, 19]


print(solution(lottos, win_nums))