class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = Node(
    1
    , Node(2, Node(4), Node(5, Node(6, None, Node(8)), Node(7)))
    , Node(3, Node(9, Node(10), Node(11)), Node(12))
)

b = Node(
    1
    , Node(2, Node(4), Node(5, Node(6, None, Node(8)), Node(7)))
    , Node(3, Node(9, Node(10), Node(11)), Node(12))
)


def check(a, b):
    if (a and not b) or (b and not a):
        return False
    if not b and not a:
        return True
    return True if a.val==b.val and check(a.right,b.right) and check(a.left,b.left) else False

l = check(a, b)
print(l)
