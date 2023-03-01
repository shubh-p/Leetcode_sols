# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1=list1
        ptr2=list2
        head=ListNode()
        new =head
        while ptr1 and ptr2:
            if ptr1.val<ptr2.val:
                new.next=ptr1
                ptr1=ptr1.next
            else:
                new.next=ptr2
                ptr2=ptr2.next
            new=new.next
        if ptr1==None and ptr2==None:
            return head.next
        elif ptr1==None:
            new.next=ptr2
        else:
            new.next=ptr1
        return head.next