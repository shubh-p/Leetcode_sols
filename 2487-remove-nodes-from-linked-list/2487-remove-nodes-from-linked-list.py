# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def remove(node):
            if node.next.next==None:
                return
            remove(node.next)
            if node.next.val<node.next.next.val:
                node.next=node.next.next
            return
        remove(head)
        if head.val<head.next.val:
            head=head.next
        return head