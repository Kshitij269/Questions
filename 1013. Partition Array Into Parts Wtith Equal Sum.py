class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        if sum(arr) % 3 != 0:
            return False

        part = sum(arr) // 3
        initial_sum = 0
        count = 0

        for i in arr:
            initial_sum += i
            if initial_sum == part:
                count += 1
                initial_sum = 0

        return (count >= 3)

