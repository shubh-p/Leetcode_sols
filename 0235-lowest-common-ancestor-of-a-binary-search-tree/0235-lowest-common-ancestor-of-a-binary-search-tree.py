# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a=min(p.val,q.val)
        b=max(p.val,q.val)
        def fn(node):
            if a<=node.val and b>=node.val:
                return node
            if a<node.val and b<node.val:
                return fn(node.left)
            if a>node.val and b>node.val:
                return fn(node.right)
            
        return fn(root)