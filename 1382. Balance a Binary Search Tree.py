class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans =[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)

        def buildTree(lst,low,high):
            if low > high :
                return None
            mid=(low+high)//2
            root = TreeNode(lst[mid])
            root.left = buildTree(lst,low,mid-1)
            root.right = buildTree(lst,mid+1,high)
            return root

        low = 0
        high = len(ans)-1
        root = buildTree(ans,low,high)
        return root