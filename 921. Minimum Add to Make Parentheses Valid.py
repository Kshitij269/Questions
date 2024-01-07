class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for i in s:
            if i=='(':
                stack.append(i)
                continue
            if i==')':
                if not stack:
                    ans+=1
                else:
                    if stack[-1]=='(':
                        stack.pop()
                continue
            ans+=1
        return ans+len(stack)