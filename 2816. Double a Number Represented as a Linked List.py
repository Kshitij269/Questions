class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = prev = ListNode(0, head)
        curr = head

        while curr:
            db = curr.val * 2
            if db > 9:
                curr.val = db - 10
                prev.val += 1
            else:
                curr.val = db

            prev = curr
            curr = curr.next

        return head if carry.val == 0 else carry