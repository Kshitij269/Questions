class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack)> 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i-index
            stack.append(i)
        return(ans)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i,temperature in enumerate(temperatures):
            if not stack:
                stack.append((temperature,i))
            else:
                while stack and temperature > stack[-1][0]:
                    tmp,index = stack.pop()
                    ans[index] = i-index
                stack.append((temperature,i))
        return ans