from collections import Counter
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        l = Counter(deck)
        values = list(l.values())
        if gcd(*values)>1:
            return 1
        return 0