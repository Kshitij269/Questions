nums = [6, 2, 6, 5, 1, 2]
ans = 0
nums = sorted(nums)
for i in range(0,len(nums),2):
        print(i,nums[i],nums[i+1])
        ans += min(nums[i],nums[i+1])
print(ans)
