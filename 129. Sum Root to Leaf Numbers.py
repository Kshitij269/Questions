class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, num):
        if not node:
            return 0

        if not node.left and not node.right:
            return num * 10 + node.val

        return self.dfs(node.left, num * 10 + node.val) + self.dfs(node.right, num * 10 + node.val)

