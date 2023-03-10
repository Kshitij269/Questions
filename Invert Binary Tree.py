from binarytree import Node
'''class Node():
    def __init__ (self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
'''
a=Node(1)
a.left=Node(2)
a.right=Node(3)
a.left.left=Node(4)
a.left.right=Node(5)

a.right.right=Node(6)
a.right.right.left=Node(7)

def solve(root):

    if root:
        solve(root.left)
        solve(root.right)
        root.left,root.right=root.right,root.left
    return root 
print(solve(a))

