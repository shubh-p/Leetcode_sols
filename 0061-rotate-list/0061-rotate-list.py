# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        tail=head
        length=1
        while tail.next:
            length+=1
            tail=tail.next
        k=k%length
        if k==0:
            return head
        tail.next=head
        ptr=head
        for i in range(length-k-1):
            ptr=ptr.next
        head=ptr.next
        ptr.next=None
        return head
        
        
        