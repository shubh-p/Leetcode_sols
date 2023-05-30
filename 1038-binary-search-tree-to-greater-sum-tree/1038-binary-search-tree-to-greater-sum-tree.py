# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def gst(node,currsum):
            if node==None:
                return currsum
            node.val+=gst(node.right,currsum)
            currsum=node.val
            if node.left:
                return gst(node.left,currsum)
            return currsum
        
        gst(root,0)
        return root