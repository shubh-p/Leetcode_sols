# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node:
                return []
            leftval=inorder(node.left)
            rightval=inorder(node.right)
            return leftval + [node.val] + rightval
        a=inorder(root)
        def bst(a):
            n=len(a)
            if n==0:
                return None
            newroot=TreeNode(a[n//2])
            newroot.left=bst(a[:n//2])
            newroot.right=bst(a[(n//2)+1:])
            return newroot
        return bst(a)

