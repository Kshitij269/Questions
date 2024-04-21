nums = [1,3,4,8,7,9,3,5,1]
k = 2

new = sorted(nums)
ans = []
for i in range(0,len(nums),3):
    if nums[i+2] - nums[i] > k:
        return []
    else :
        ans.append(nums[i:i+3])
    return ans
