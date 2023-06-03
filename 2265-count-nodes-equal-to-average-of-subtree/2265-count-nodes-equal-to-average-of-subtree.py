# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def rec(node,count):
            if not node:
                return 0,0
            leftsum,lc=rec(node.left,count)
            rightsum,rc=rec(node.right,count)
            count=lc+rc+1
            sum=node.val+leftsum+rightsum
            if node.val==sum//count:
                nonlocal ans
                ans+=1
            return sum,count


        totalsum=rec(root,0)
        print(totalsum)
        return ans
