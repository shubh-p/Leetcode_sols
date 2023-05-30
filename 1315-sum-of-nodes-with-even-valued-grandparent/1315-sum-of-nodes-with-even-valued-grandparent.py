# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=0
        def fn(node):
            if node:
                nonlocal ans
                ans+=node.val
        def sum(node):
            if not node:
                return 
            if node.val%2==0:
                if node.left:
                    fn(node.left.left)
                    fn(node.left.right)
                if node.right:
                    fn(node.right.left)
                    fn(node.right.right)
            sum(node.left)
            sum(node.right)

        sum(root)
        return ans        
            