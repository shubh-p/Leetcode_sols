# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node,n):
            if node==None:
                return n
            return max(depth(node.left,n+1),depth(node.right,n+1))
        return depth(root,0)