from binarytree import Node
# class Node():
#     def __init__(self,data,left=None,right=None):
#         self.data=data
#         self.left=left
#         self.right=right

a=Node(2)
a.left=Node(3)
a.right=Node(4)
a.left.left=Node(5)
a.left.right=Node(6)
a.right.left=Node(7)
a.right.right=Node(8)

def checkLeft(root):
    if root is None:
        return
    while root.left is not None :
        root=root.left
    return root

def printleaf(root):
    if root is None:
        return
    if (root.left is None) and (root.right is None ):
        print(root.data)

    printleaf(checkLeft(root.left))
    printleaf(checkLeft(root.right))

print(a)
