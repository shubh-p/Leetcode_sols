# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            elif node.val==p.val or node.val==q.val:
                return node
            a=dfs(node.left)
            b=dfs(node.right)
            if not a and not b:
                return None
            if a and not b:
                return a
            if b and not a :
                return b
            if a and b:
                return node
        return dfs(root)

