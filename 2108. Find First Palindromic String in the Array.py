class Solution:
    def firstPalindrome(self, a: List[str]) -> str:
        return next(filter(lambda w:w==w[::-1],a),'')
