# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node,curr=head.next,head
        sum=0
        while node:
            if node.val==0:
                curr.val=sum
                if node.next==None:
                    # print(curr.val)
                    curr.next=None
                    break
                curr=curr.next
                sum=0
            sum+=node.val
            node=node.next

        return head
            
                