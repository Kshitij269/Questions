def missing_number(nums):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == nums[mid]:
            lo = mid + 1
        elif mid != nums[mid]:
            hi = mid - 1
    return hi + 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        return missing_number(nums)
