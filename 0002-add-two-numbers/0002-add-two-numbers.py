# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1,ptr2=l1,l2
        a,b=0,0
        sum,flag=0,0
        while ptr1:
            ptr1=ptr1.next
            a+=1
        while ptr2:
            ptr2=ptr2.next
            b+=1
        if a>=b:
            ans=ptr1=l1
            ptr2=l2
        else:
            ans=ptr1=l2
            ptr2=l1
        #print(ptr1,ptr2)
        while ptr1:
            a=ptr1.val
            if flag==1:
                b=0
            else:
                b=ptr2.val
            sum=a+b
            if sum>9:
                if ptr1.next==None:
                    ptr1.next=ListNode(1)
                else:
                    ptr1.next.val+=1
                sum=sum%10
            ptr1.val=sum
            ptr1=ptr1.next
            if ptr2.next:
                ptr2=ptr2.next
            else:
                flag=1
        return ans