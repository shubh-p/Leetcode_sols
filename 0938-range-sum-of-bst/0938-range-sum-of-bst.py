# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def rec(node):
            nonlocal ans
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)
            if node.val in range(low,high+1):
                ans+=node.val
        rec(root)
        return ans