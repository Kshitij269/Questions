class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        heapify(nums)
        while True:
            if nums[0] >= k:
                break

            l1 = heappop(nums)
            l2 = heappop(nums)
            add = min(l1, l2) * 2 + max(l1, l2)
            heappush(nums, add)
            cnt += 1

        return cnt
