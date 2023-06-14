# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(node):
            if val<node.val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left=TreeNode(val)
                    return
            elif val>node.val:
                if node.right:
                    dfs(node.right)
                else:
                    node.right=TreeNode(val)
                    return
                    
        dfs(root)
        return root