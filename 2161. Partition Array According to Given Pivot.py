class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        ans = [pivot] * n

        for i in range(n):
            j = n - i - 1

            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1

            if nums[j] > pivot:
                ans[right] = nums[j]
                right -= 1

        return ans
