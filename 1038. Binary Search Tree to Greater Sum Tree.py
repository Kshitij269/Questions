class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = []
        val = 0
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            val += curr.val
            curr.val = val
            curr = curr.left

        return root