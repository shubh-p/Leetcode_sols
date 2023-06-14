# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        # print(ans)
        for i in range(1,len(ans)):
            # print(ans[i],ans[i-1])
            if ans[i]<=ans[i-1]:
                return False
        return True