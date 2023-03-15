class Solution:

    def count_Node(self,head):
        c=0
        while head:
            c+=1
            head=head.next
        return c

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            node=head
            l=self.count_Node(node)
            n=l//2
            c=0
            
            if l <= 1: 
                return None
            else:
                while c<n-1:
                    node = node.next
                    c+=1
                f=node.next.next
                node.next=f
                return head 

