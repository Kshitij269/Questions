class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = []

        def dfs(node, cur):
            nonlocal stack

            if node is None:
                return
            curr = cur + [node.val]

            if node.left is None and node.right is None:
                if sum(curr) == targetSum:
                    stack.append(curr)

                return

            return dfs(node.left, curr) or dfs(node.right, curr)

        dfs(root, [])
        return stack