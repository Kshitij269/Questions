# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        temp = head
        ans = True
        while temp and prev:
            if temp.val == prev.val:
                temp = temp.next
                prev = prev.next
            else:
                return False

        return ans  