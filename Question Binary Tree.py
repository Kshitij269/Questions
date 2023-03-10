class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = Node(
    10
    , Node(5, Node(3, Node(1)), Node(7, Node(6)))
    , Node(15, Node(13), Node(18))
)

sum1 = 0


class Solution:
    def rangeSumBST(self, root, low, high):
        global sum1
        if root:
            if low <= root.val <= high:
                sum1 += root.val
        if root.left:
            self.rangeSumBST(root.left, low, high)
        if root.right:
            self.rangeSumBST(root.right, low, high)
        return sum1


l = Solution()
n=l.rangeSumBST(a, 6, 10)
print(n)
