"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return head
        ptr=head
        a={}
        while ptr:
            a[ptr]=Node(ptr.val)
            ptr=ptr.next
        ptr=head
        while ptr:
            if ptr.next==None:
                a[ptr].next=None
            else:
                a[ptr].next=a[ptr.next]
            if ptr.random==None:
                a[ptr].random=None
            else:
                a[ptr].random=a[ptr.random]
            ptr=ptr.next
        return a[head]        