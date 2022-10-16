def solution(participant, completion):
    for i in range(0,len(participant)):
        for j in completion:
            if j == participant[i]:
                del participant[i]

    
    return participant

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))