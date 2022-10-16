m1 = [1,2,3,4,5]
m2 = [2,1,2,3,2,4,2,5]#홀수는 2
m3 = [3,3,1,1,2,2,4,4,5,5]

score = [0,0,0]
result = []

ans = [1,2,3,4,5]

# for idx,answer in enumerate(ans):
#     if answer == m1[idx%len(m1)]:
#         score[0] += 1
#     if answer == m2[idx%len(m2)]:
#         score[1] += 1
#     if answer == m3[idx%len(m3)]:
#         score[2] += 1

# for idx,s in enumerate(score):
#     if s == max(score):
#         result.append(idx+1)

# print(result)

def solution(answers):
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]#홀수는 2
    m3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0,0,0]
    result = []
    for idx,answer in enumerate(answers):
        if answer == m1[idx%len(m1)]:
            score[0] += 1
        if answer == m2[idx%len(m2)]:
            score[1] += 1
        if answer == m3[idx%len(m3)]:
            score[2] += 1

    for idx,s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    
    return result

print(solution(ans))