class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        root.parent = None
        root.grandparent = None
        ans = 0
        stack = [root]

        while len(stack):
            node = stack.pop()

            if node.left:
                node.left.parent = node
                node.left.grandparent = node.parent
                stack.append(node.left)

            if node.right:
                node.right.parent = node
                node.right.grandparent = node.parent
                stack.append(node.right)

            if node.grandparent and node.grandparent.val % 2 == 0:
                ans += node.val

        return ans