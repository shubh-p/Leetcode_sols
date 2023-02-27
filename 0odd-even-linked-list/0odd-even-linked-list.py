# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        optr=head
        eptr=head.next
        even=head.next
        while optr and eptr:
            if optr.next.next==None:
                break
            optr.next=optr.next.next
            eptr.next=eptr.next.next
            optr=optr.next
            eptr=eptr.next
        optr.next=even
        return head
        