from binarytree import Node

root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.right.left = Node("D")
root.right.left.right = Node("F")

root.right.right = Node("E")
root.right.right.right = Node("G")
print(root)
print(root.inorder)
