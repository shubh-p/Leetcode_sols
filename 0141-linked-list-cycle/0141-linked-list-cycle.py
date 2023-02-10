# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        slow=head.next
        if slow==None:
            return False
        fast=head.next.next
        if fast==None:
            return False
        while slow!=fast:
            if fast.next==None or fast.next.next==None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True