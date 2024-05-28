class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = 0
        rightSum = 0
        ans = 0
        for i in range(k):
            leftSum += cardPoints[i]
        maxSum = leftSum

        right_idx = len(cardPoints) - 1

        for i in range(k - 1, -1, -1):
            leftSum -= cardPoints[i]
            rightSum = rightSum + cardPoints[right_idx]
            right_idx -= 1

            maxSum = max(maxSum, leftSum + rightSum)

        return maxSum