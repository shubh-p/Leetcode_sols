# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        ans=head.next
        def swap(node):
            if node==None or node.next==None:
                return 
            temp=node.next.next
            node.next.next=node
            # node.next=temp==None ? None ?: 
            if temp==None:
                node.next=None
            elif temp.next==None:
                node.next=temp
            else:
                node.next=temp.next
            return swap(temp)
        swap(head)
        return ans