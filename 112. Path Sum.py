class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, sum1):
            if node is None:
                return False

            if node.left is None and node.right is None and sum1 + node.val == targetSum:
                return True

            return dfs(node.left, sum1 + node.val) or dfs(node.right, sum1 + node.val)

        return dfs(root, 0)
