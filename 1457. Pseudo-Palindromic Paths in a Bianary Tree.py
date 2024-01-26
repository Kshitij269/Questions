from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        ans = 0
        count = defaultdict(int)

        def printRoute(root):
            nonlocal ans, count 
            count[root.val] += 1

            if root.left is None and root.right is None:
                odds = 0
                for key in count :
                    if count[key]%2:
                        odds+=1
                        if odds>1:
                            break 
                if odds<=1:
                    ans +=1

            if root.left:
                printRoute(root.left)
            if root.right:
                printRoute(root.right)
            count[root.val]-=1

        printRoute(root)
        return ans