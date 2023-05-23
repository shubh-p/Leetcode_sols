# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height=0
        def fn(root,height):
            if root==None:
                return 0
            height+=max(fn(root.left,height),fn(root.right,height))+1
            return height
        return fn(root,0)
        