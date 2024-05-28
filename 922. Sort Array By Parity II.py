class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        even = 0
        odd = 1
        for num in nums:
            if num % 2 == 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd += 2

        return ans


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1

        while even < len(nums) and odd < len(nums):
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2
            while odd < len(nums) and nums[odd] % 2 != 0:
                odd += 2

            if even < len(nums) and odd < len(nums):
                nums[even], nums[odd] = nums[odd], nums[even]

            even += 2
            odd += 2

        return nums
