s = "(()())(())"
result = ""
stack = []
closed = 0
opened = 0
for i in s:
    if i == "(":
        opened += 1
    elif i == ")":
        closed += 1
    print("opened",opened,"closed",closed)

    if opened == closed and i == ")":
        stack.append(i)
    elif opened > closed:
        stack.append(i)
    print(stack)


class Solution:
    # Can you find the primitive decomposition? The number of ( and ) characters must be equal.
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        closed = -1
        opened = -1
        current_primitive = ""

        for i in s:
            if i == "(":
                opened += 1
            elif i == ")":
                closed += 1

            current_primitive += i

            if opened == closed:
                result += current_primitive[1:-1]  # Remove outer parentheses
                current_primitive = ""
                opened = 0
                closed = 0

        return result
