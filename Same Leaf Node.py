class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

a=Node(3,
       Node(5,Node(6),Node(2,Node(7),Node(4))),
       Node(1,Node(9),Node(8)))

b=Node(3,
       Node(5,Node(6),Node(2,Node(7),Node(4))),
       Node(1,Node(9),Node(8)))

n1=[]
n2=[]

def solution(root,n):
    if (root is not None) :
        if (root.left is None) and (root.right is None):
            n.append(root.val)
        solution(root.left,n)
        solution(root.right,n)
    return n

l1=solution(a,n1)
l2=solution(b,n2)
print(l1,l2)