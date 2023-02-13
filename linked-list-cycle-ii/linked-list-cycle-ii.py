# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a={}
        count=0
        ptr=head
        while(ptr !=None):
            if ptr in a:
                return ptr
            a[ptr]=count
            count+=1
            ptr=ptr.next
        return None