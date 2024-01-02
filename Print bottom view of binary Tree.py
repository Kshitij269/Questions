class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def printBottomView(root):
    d = dict()
    printBottomViewUtil(root, d, 0, 0)
    for i in sorted(d.keys()):
        print(d[i][0], end=" ")

def printBottomViewUtil(root, d, hd, level):
    if root is None:
        return

    if hd in d:
        if level >= d[hd][1]:
            d[hd] = [root.data, level]

    else:
        d[hd] = [root.data, level]

    printBottomViewUtil(root.left, d, hd - 1, level + 1)

    printBottomViewUtil(root.right, d, hd + 1, level + 1)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printBottomView(root)
