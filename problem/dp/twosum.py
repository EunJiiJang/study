nums = [2,7,11,15]
target = 9
nums.sort()
l,r =0,len(nums)-1
while not nums[l]==nums[r]:
    if nums[l]+nums[r] > target:
        r -= 1
    elif nums[l]+nums[r] < target:
        l += 1
    else:
        print(nums[l],nums[r])
        break