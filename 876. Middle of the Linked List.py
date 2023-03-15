class Solution:
    
    def Length(self,head):
        cnt = 0 
        while head is not None :
            cnt+=1
            head=head.next
        return cnt
    
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.Length(head)
        c=(length//2)+1
        while c>1:
            head=head.next
            c-=1
        return head
