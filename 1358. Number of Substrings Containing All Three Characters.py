class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {"a": 0, "b": 0, "c": 0}
        n = len(s)
        left = 0
        ans = 0

        for right in range(len(s)):
            cnt[s[right]] += 1
            while (cnt['a'] and cnt['b'] and cnt['c']):
                ans += n - right
                cnt[s[left]] -= 1
                left += 1

        return ans