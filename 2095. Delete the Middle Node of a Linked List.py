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

            # Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = fast = curr = head
        curr = None
        while fast and fast.next is not None:
            curr = slow
            slow = slow.next
            fast = fast.next.next

        if curr:
            curr.next = slow.next
        else:
            head = head.next

        return head


