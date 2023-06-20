# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fn(a):
            n=len(a)
            if n==0:
                return None
            root=TreeNode(a[n//2])
            root.left=fn(a[:n//2])
            root.right=fn(a[n//2+1:])
            return root


        return fn(nums)


            