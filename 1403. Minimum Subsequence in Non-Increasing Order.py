class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sum = 0
        heap = []
        for num in nums:
            sum += num
            heappush(heap, -num)

        result = []
        current = 0

        while current <= sum:
            largest = -heappop(heap)
            current += largest
            result.append(largest)
            sum -= largest

        return result