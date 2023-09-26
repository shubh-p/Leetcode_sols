# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        mmax=sys.maxsize
        i=0
        def rec(mmax):
            nonlocal i
            if i==len(preorder) or preorder[i]>mmax:
                return None
            node=TreeNode(preorder[i])
            i+=1
            node.left=rec(node.val)
            node.right=rec(mmax)
            return node

        return rec(mmax)
