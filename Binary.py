import binarytree
class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = Node(
    "A"
    , Node("B", Node("D"), Node("E", Node("H", None, Node("L")), Node("I")))
    , Node("C", Node("F", Node("J"), Node("K")), Node("G"))
)
s = ""


def concatenate(root):
    global s
    if root:
        s = s + " " + root.data
    if root.left:
        concatenate(root.left)
    if root.right:
        concatenate(root.right)
    return s


l = concatenate(a)

print(l)
