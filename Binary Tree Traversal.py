class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = Node("A",
         Node("B", Node("D"), Node("E", Node("H", None, Node("L")), Node("I"))),
         Node("C", Node("F", Node("J"), Node("K")), Node("G"))
         )


# a=Node("A",Node("B",Node("D"),Node("E")),Node("C",Node("F"),Node("G")))

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


preorder(a)
print()
inorder(a)
print()
postorder(a)
