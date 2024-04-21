class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True

        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next

        return False