from heapq import heapify,heappop,heappush
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        heap = []
        for i in nums :
           if i!=0:
               heappush(heap,i)
        return len(set(heap))
