class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    indices.add(i)

        indices.update(stack)
        result = []
        for i, char in enumerate(s):
            if i not in indices:
                result.append(char)

        return ''.join(result)