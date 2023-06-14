"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans=0
        def dfs(node):
            if not node.children:
                return 1
            depth=[]
            for child in node.children:
                depth.append(1+dfs(child))
            return max(depth)
                
        return dfs(root)