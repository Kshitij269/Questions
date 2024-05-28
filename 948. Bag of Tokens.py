class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, max_score = 0, 0
        low = 0
        high = len(tokens) - 1
        while low <= high:

            if tokens[low] <= power:
                power -= tokens[low]
                score += 1
                max_score = max(max_score, score)
                low += 1
            elif score > 0:
                power += tokens[high]
                score -= 1
                high -= 1

            else:
                break
        return max_score
