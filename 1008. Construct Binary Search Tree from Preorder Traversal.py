class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        parent = root
        stack = [parent]

        for x in preorder[1:]:
            newNode = TreeNode(v)
            if stack and newNode.val < parent.val:
                parent.left = newNode
                stack.append(newNode)
                parent = newNode

            else:
                while stack and stack[-1] < newNode.val:
                    parent = stack.pop()

                parent.right = newNode
                stack.append(newNode)
                parent = newNode

            return root

