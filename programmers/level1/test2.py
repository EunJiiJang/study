from itertools import chain, combinations
import itertools
def solution(call):
    answer = ''
    call_lower = call.lower()
    call_list = list(call_lower)
    total_list = chain.from_iterable(combinations(call_list, r) for r in range(2, len(call_list + 1)))
    print(call_list)
    
    return answer





call = "abcabcdefabc"
call_lower = call.lower()
call_list = list(call_lower)
#total_list = itertools.permutations((call_lower, r) for r in range(1, len(call_lower + 1)))
total_list = list(itertools.permutations((call_lower,r )for r in range(1, len(call_lower)+1)))
print(total_list)

#print(solution(call))