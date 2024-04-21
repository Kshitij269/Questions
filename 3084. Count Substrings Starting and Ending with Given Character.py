class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        l = s.count(c)
        return (l*(l+1))//2