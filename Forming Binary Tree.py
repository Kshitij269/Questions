class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
a=Node(1,
       Node(2,Node(4),Node(5,None,Node(8))),
       Node(3,Node(6,Node(9)),Node(7)))

b=Node(1,
       Node(2,Node(4),Node(5)),
       Node(3,Node(6),Node(7))
      )

c=Node("A",
       Node("B",Node("D"),Node("E",Node("H",None,Node("L")),Node("I"))),
       Node("C",Node("F",Node("J"),Node("K")),Node("G"))
      )
