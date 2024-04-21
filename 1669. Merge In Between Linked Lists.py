class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1 = list1
        curr2 = list1
        for i in range(a - 1):
            curr1 = curr1.next

        for i in range(b + 1):
            curr2 = curr2.next

        next_node = curr2.next

        curr1.next = list2

        while list2.next is not None:
            list2 = list2.next
        list2.next = curr2

        return list1
