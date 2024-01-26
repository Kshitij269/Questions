class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, max1, min1):
            max1 = max(max1, node.val)
            min1 = min(min1, node.val)

            self.ans = max(self.ans, abs(max1 - min1))
            if node.left:
                dfs(node.left, max1, min1)
            if node.right:
                dfs(node.right, max1, min1)

        dfs(root, root.val, root.val)
        return self.ans