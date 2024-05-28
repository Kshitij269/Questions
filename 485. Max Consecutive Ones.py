class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                right += 1

            else:
                ans = max(ans, right - left)
                right += 1
                left = right

        ans = max(ans, right - left)
        return ans
    