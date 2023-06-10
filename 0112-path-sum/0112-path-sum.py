# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum=0
        ans=False
        def dfs(node,sum):
            if not node:
                return
            sum+=node.val
            # print(node.val,sum)
            if not node.left and not node.right and sum==targetSum:
                nonlocal ans
                ans=True
                # print("found")
                return 
            dfs(node.left,sum)
            dfs(node.right,sum)
            
        dfs(root,0)
        return ans
                