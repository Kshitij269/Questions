nums = [-2,9,9,8,4]
k =  5

nums.sort()
for i in range(k):
    if nums[0] != 0:
        nums[0] = -nums[0]
        nums.sort()
    else:
        break

print(sum(nums))
