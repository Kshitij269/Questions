# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node
            return prev

        slow = fast = curr = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        l = reverse(slow)

        while l is not None and curr is not None:
            if l.val != curr.val:
                return False
            l = l.next
            curr = curr.next

        return True
