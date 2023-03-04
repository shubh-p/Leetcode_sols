class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return head
        truehead=head
        def flattene(head: 'Optional[Node]') -> 'Optional[Node]':
            ptr=head
            currhead=head
            while ptr:
                if ptr.child:
                    temp=flattene(ptr.child)
                    if temp:
                        temp.prev.next=ptr.next
                        if ptr.next:
                            ptr.next.prev=temp.prev
                        ptr.next=temp
                        ptr.child=None
                        ptr.next.prev=ptr
                if not ptr.next:
                    break
                ptr=ptr.next
            if currhead!=truehead:
                currhead.prev=ptr
            return currhead
        return flattene(head)
