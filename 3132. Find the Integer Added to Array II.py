class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = float("inf")
        n = len(nums1)

        for i in range(n):
            for j in range(i + 1, n):
                l = nums1[:i] + nums1[i + 1:j] + nums1[j + 1:]
                diff = nums2[0] - l[0]

                if all(x - y == diff for x, y in zip(nums2, l)):
                    ans = min(ans, diff)

        return ans