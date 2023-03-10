class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 1:
            return [-1]

        i = 0

        while i < len(arr) - 1:
            max_val = max(arr[i + 1:])
            arr[i] = max_val

            i += 1

        arr[i] = -1

        return arr