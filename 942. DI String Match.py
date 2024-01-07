class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low = 0
        high = len(S)
        ans = []
        for i in S:
            if i == 'I':
                ans.append(low)
                low+=1
            else:
                ans.append(high)
                high-=1
        ans.append(low)
        return ans 