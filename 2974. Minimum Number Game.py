import heapq


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        heapq.heapify(nums)
        while nums:
            l1 = heapq.heappop(nums)
            l2 = heapq.heappop(nums)
            ans.extend([l2, l1])

        return ans