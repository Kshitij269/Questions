# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count_node(self,head):
        cnt=0
        while head:
            cnt+=1
            head=head.next
        return cnt
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=self.count_node(head)
        if l<=1:
            return head
        else:
            node=head
            while node is not None and node.next is not None :
                node.val,node.next.val=node.next.val,node.val
                node=node.next.next
            return head

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first_node = head
            second_node = head.next

            # Swapping
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Move pointers forward
            prev = first_node
            head = first_node.next

        return dummy.next