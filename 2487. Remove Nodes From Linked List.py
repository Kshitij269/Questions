class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node
            return prev

        l = reverse(head)
        curr = l
        max_value = float("-inf")
        dummy = None
        while curr is not None:
            max_value = max(max_value, curr.val)
            if curr.val < max_value:
                if dummy:
                    dummy.next = curr.next
                else:
                    l = curr.next
            else:
                dummy = curr

            curr = curr.next

        return reverse(l)