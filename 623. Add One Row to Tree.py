class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        curr = 1
        return self.add(root, val, depth, curr)

    def add(self, root, val, depth, curr):
        if (root == None):
            return None

        if (curr == depth - 1):
            leftTemp = root.left
            rightTemp = root.right

            root.left = TreeNode(val)
            root.right = TreeNode(val)

            root.left.left = leftTemp
            root.right.right = rightTemp

            return root

        root.left = self.add(root.left, val, depth, curr + 1)
        root.right = self.add(root.right, val, depth, curr + 1)

        return root
