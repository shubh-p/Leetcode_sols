# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,ans):
            if not node:
                return
            dfs(node.left,ans)
            if not node.left and not node.right:
                ans.append(node.val)
            dfs(node.right,ans)
        nodes1,nodes2=[],[]
        dfs(root1,nodes1)
        dfs(root2,nodes2)
        # print(nodes1)
        # print(nodes2)
        return nodes1==nodes2