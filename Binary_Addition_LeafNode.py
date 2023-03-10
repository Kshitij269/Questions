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
    if root.left:
        evalbinary(root.left)
    if root.right:
        evalbinary(root.right)
    
    if root:
        if root.data==2:
            print(root.left.data,root.right.data,s)
            s= root.left.data or root.right.data
        elif root.data==3:
            print(root.left.data,root.right.data,s)
            s= root.left.data and root.right.data       
    return s


l = evalbinary(a)
print(l)
