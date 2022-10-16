numbers = [100,101,102,103,104]
start = [1,2]
finish = [2,4]

def solution(numbers, start, finish):
    answer = []
    for i in range(0,len(start)):
        answer.append(sum(numbers[start[i]:finish[i]+1]))
    return answer



print(solution(numbers,start,finish))