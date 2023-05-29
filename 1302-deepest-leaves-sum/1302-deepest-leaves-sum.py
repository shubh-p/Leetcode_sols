# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=collections.deque()
        q.append(root)
        ans=root.val
        prev=ans
        while q:
            prev=ans
            ans=0
            for i in range(len(q)):
                curr=q.popleft()
                if curr==None:
                    continue
                ans+=curr.val
                q.append(curr.left)
                q.append(curr.right)
                
        return prev
            