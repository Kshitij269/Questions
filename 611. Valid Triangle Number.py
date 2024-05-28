class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            low = 0
            high = i - 1
            while (low < high):
                if (nums[low] + nums[high] > nums[i]):
                    ans += (high - low)
                    high -= 1
                else:
                    low += 1

        return ans 
