class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = [-i for i in nums]
        heapq.heapify(l)
        m1 = -1*heapq.heappop(l)
        m2 = -1*heapq.heappop(l)

        return (m1-1)*(m2-1)
