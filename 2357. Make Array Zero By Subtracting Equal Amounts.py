from heapq import heapify,heappop,heappush
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        heap = []
        for i in nums :
           if i!=0:
               heappush(heap,i)
        return len(set(heap))


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums = [i for i in nums if i > 0]
        heapify(nums)

        while len(nums) > 0:
            smallest = heappop(nums)
            nums = [num - smallest for num in nums if num != smallest]
            ans += 1

        return ans