# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(nums):
            if not nums:
                return None
            m=max(nums)
            i=nums.index(m)
            root=TreeNode(m)
            root.left=rec(nums[:i])
            root.right=rec(nums[i+1:])
            return root
        
        return rec(nums)