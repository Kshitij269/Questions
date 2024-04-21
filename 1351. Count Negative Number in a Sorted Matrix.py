class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for g in grid:
            left, right = 0, len(g)
            while left < right:
                mid = left + (right - left) // 2
                if g[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid

            count += len(g) - left
        return count