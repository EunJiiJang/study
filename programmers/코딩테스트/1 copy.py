numbers = [100,101,102,103,104]
start = [1,2]
finish = [2,4]

def solution(numbers, start, finish):
    answer = []
    cnt = 0
    while cnt < len(start):
        answer.append(sum(numbers[start[cnt]:finish[cnt]+1]))
        cnt += 1
    return answer


print(solution(numbers,start,finish))