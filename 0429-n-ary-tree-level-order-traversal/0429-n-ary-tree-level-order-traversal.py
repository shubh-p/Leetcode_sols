"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        ans=[]
        q=deque()
        q.append(root)
        
        while q:
            temp=[]
            for i in range(len(q)):
                curr=q.popleft()
                temp.append(curr.val)
                for child in curr.children:
                    if child:
                        q.append(child)
            ans.append(temp)
        return ans