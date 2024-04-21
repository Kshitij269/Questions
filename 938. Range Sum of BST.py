class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if node is None:
                return 0

            if low <= node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
            elif node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

        return dfs(root)
