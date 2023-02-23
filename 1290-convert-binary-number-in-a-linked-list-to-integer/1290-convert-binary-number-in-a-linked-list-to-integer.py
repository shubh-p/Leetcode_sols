# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr=head
        sum=0
        while ptr:
            sum*=2
            sum+=ptr.val
            ptr=ptr.next
        return sum