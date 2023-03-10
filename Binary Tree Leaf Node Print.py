class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = Node(
    1
    , Node(2, Node(4), Node(5, Node(6, None, Node(8)), Node(7)))
    , Node(3, Node(9, Node(10), Node(11)), Node(12))
)
print(a)



def sumofnode(root):
    global sum1
    if root and root.left is None and root.right is None:
        print(root.data)
    if root.left:
        sumofnode(root.left)
    if root.right:
        sumofnode(root.right)


l = sumofnode(a)
