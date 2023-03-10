class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root = Node("A",
            Node("B"),
            Node("C", Node("D", None, Node("F")), Node("E", None, Node("G")))
            )
