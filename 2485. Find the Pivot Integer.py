import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = (n + 1) * n / 2
        pivot = int(math.sqrt(sum))
        if pivot * pivot == sum :
            return pivot
        return -1

