# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if node==None:
                return None
            elif node.val==val:
                return node
            elif val<node.val:
                return search(node.left)
            else:
                return search(node.right)

        return search(root)