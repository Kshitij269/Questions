class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(len(nums)-2,-1,-1):
            nums[i]=max(nums[i],nums[i]+nums[i+1])
        nums.sort()
        return nums[-1]