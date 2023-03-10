
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = Node(2
    , Node(1)
    , Node(3, Node(0), Node(1))
)


s=0
def evalbinary(root):
    global s
    if root and root.left is None and root.right is None:
        s+=root.data
    if root.left:
        evalbinary(root.left)
    if root.right:
        evalbinary(root.right)
    return s


l = evalbinary(a)
print(l)
