class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        i = 0
        j = 1
        k = 2
        ans = 0

        while i < n and j < n and k < n:
            if nums[k] - nums[j] < diff:
                k += 1

            elif nums[j] - nums[i] < diff:
                j += 1

            elif (nums[k] - nums[j] == diff) and (nums[j] - nums[i] == diff):
                ans += 1
                k += 1
            else:
                i += 1

        return ans