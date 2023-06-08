# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans1=[]
        ans2=[]
        def dfs1(node):
            if not node:
                ans1.append("None")
                return 
            ans1.append(node.val)
            dfs1(node.left)
            dfs1(node.right)
        def dfs2(node):
            if not node:
                ans2.append("None")
                return 
            ans2.append(node.val)
            dfs2(node.right)
            dfs2(node.left)
        dfs1(root.left)
        dfs2(root.right)
        return ans1==ans2
        