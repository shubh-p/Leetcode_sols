# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptr=head
        count=0
        while ptr:
            count+=1
            ptr=ptr.next
        if count==1:
            return True
       # if count%2==1:
        #    return False
        prev=None
        curr=head
        for i in range(int(count/2)):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        if count%2==1:
            curr=curr.next
        for i in range(int(count/2)):
            if curr.val != prev.val:
                return False
            curr=curr.next
            prev=prev.next
        return True
