# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node=head
        ans=[]
        while node:
            ans.append(node.val)
            node=node.next
        m=-1
        n=len(ans)
        for i in range(n//2):
            m=max(m,ans[i]+ans[n-1-i])
        return m
        