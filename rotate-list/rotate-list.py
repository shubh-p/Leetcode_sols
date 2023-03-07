# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        ptr=head
        length=0
        while ptr:
            length+=1
            ptr=ptr.next
        k=k%length
        if k==0:
            return head
        ptr=head
        count=1
        while ptr:
            if count==length-k:
                newhead=ptr.next
                ptr.next=None
                temp=newhead
                for i in range(k-1):
                    temp=temp.next
                temp.next=head
                head=newhead
            ptr=ptr.next
            count+=1
        return newhead