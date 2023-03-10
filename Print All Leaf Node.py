class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

a=Node(2)
a.left=Node(3)
a.right=Node(4)
a.left.left=Node(5)
a.left.right=Node(6)

def printleaf(root):
    if root is None:
        return
    if (root.left is None) and (root.right is None ):
        print(root.data)

    printleaf(root.left)
    printleaf(root.right)

printleaf(a)

