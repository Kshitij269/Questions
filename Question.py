

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

l=[]
i=0

while head:
    s=0
    if head.data==0:

        head=head.next
        while head is not None and head.data!=0:

            s+=head.data
            head=head.next
        l.append(s)


print(l[0:len(l)-1])



