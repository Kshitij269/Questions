class Solution:
    def count_node(self,head):
        c=0
        while(head):
            c+=1
            head=head.next
        return c
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1=head
        node2=head
        c1,c2,c=1,1,self.count_node(head)+1-k

        while c1<k:
            node1=node1.next
            c1+=1
        
        while c2<c:
            node2=node2.next
            c2+=1
    
        node1.val,node2.val=node2.val,node1.val

        return head

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            fast = slow = head

            for _ in range(k - 1):
                fast = fast.next

            first = fast
            while fast and fast.next:
                fast = fast.next
                slow = slow.next

            temp = first.val
            first.val = slow.val
            slow.val = temp
            return head

    
