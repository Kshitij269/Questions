class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while head is not None and head.next is not None:
            l = head.next
            val1 = head.val
            val2 = head.next.val
            node = ListNode(math.gcd(val1, val2))
            head.next = node
            node.next = l

            head = head.next.next

        return curr

