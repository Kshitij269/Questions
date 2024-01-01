class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)

        if leftDepth == rightDepth:
            return root
        else:
            if leftDepth > rightDepth:
                return self.subtreeWithAllDeepest(root.left)
            else:
                return self.subtreeWithAllDeepest(root.right)

    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))