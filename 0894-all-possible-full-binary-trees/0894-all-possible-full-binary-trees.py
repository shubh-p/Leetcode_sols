# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp={}
        def rec(n):
            if n==0:
                return []
            if n==1:
                return [TreeNode(0)]
            if n in dp:
                return dp[n]
            ans=[]
            for l in range(n):
                left,right=rec(l),rec(n-1-l)
                for t1 in left:
                    for t2 in right:                     
                        ans.append(TreeNode(0,t1,t2))
            dp[n]=ans
            return ans
        return rec(n)