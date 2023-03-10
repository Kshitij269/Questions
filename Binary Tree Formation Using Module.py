from binarytree import Node
root=Node('A')
root.left=Node('B')
root.left.left=Node('D')
root.left.right=Node('E')
root.left.right.left=Node('H')
root.left.right.right=Node('I')
root.left.right.left.right=Node('L')

root.right=Node('C')
root.right.right=Node('G')
root.right.left=Node('F')
root.right.left.left=Node('J')
root.right.left.right=Node('K')

print(root)