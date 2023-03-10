class Node():
    def __int__(self,data,left=None.,right=None):
        self.data=data
        self.left=left
        self.right=right

a=Node(1,Node(2,Node(3),Node(4)),Node(2,Node(4),Node(3)))
