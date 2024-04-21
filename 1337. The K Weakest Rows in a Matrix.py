class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        arr = []
        for i in range(len(mat)):
            heapq.heappush(arr, (sum(mat[i]), i))

        ans = []
        while k > 0:
            node, i = heapq.heappop(arr)
            ans.append(i)
            k -= 1

        return ans


