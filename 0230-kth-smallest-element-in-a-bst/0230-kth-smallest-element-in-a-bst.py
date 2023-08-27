# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=[]
        count=0
        def rec(node):
            if not node:
                return 
            rec(node.left)
            a.append(node.val)
            rec(node.right)
        rec(root)
        return a[k-1]