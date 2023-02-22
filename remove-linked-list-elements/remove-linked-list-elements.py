# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return head
        while head.val==val:
            head=head.next
            if head==None:
                return head
            
        prev=head
        ptr=prev.next
        while ptr:
            if ptr.val==val:
                prev.next=ptr.next
                ptr=ptr.next
            else:
                prev=ptr
                ptr=ptr.next    
        return head