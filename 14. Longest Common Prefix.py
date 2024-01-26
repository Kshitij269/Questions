class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first, last = min(strs), max(strs)
        ans = ''

        for i in range(min(len(first), len(last))):

            if first[i] != last[i]:
                break
            ans += first[i]

        return ans


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(left, right):
            mins = min(len(left), len(right))

            for i in range(mins):
                if left[i] != right[i]:
                    return left[0:i]

            return left[0:mins]

        def longestCommonPrefix(strs, l, r):
            if (l == r):
                return strs[l]
            else:
                mid = int((l + r) / 2)
                left = longestCommonPrefix(strs, l, mid)
                right = longestCommonPrefix(strs, mid + 1, r)
                return commonPrefix(left, right)

        if strs is None or len(strs) == 0:
            return ""
        return longestCommonPrefix(strs, 0, len(strs) - 1)

