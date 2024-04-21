class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = 0
        max_drink = 0

        while total > 0:
            max_drink += total
            empty += total
            total = 0
            if empty // numExchange > 0:
                total += 1
                empty -= numExchange
                numExchange += 1

        return max_drink