class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root, "")

    def dfs(self, node, curr_string):
        curr_string = chr(ord('a') + node.val) + curr_string

        if node.left is None and node.right is None:
            return curr_string

        elif node.left is None:
            return self.dfs(node.right, curr_string)

        elif node.right is None:
            return self.dfs(node.left, curr_string)

        else:
            return min(self.dfs(node.left, curr_string), self.dfs(node.right, curr_string))


