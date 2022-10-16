def solution(nums):
    lst = set(nums)
    answer = 0
    
    if len(lst) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(lst)
    return int(answer)


def bestSolution(nums):
    return min(len(nums)/2 ,len(set(nums)))
 
nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]

# print(solution(nums3))

print(bestSolution(nums3))