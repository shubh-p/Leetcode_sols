# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q=deque()
        q.append(root)
        ans=-sys.maxsize
        # print(ans)
        level=0
        lvl=0
        while q:
            sum=0
            level+=1
            for i in range(len(q)):
                curr=q.popleft()
                sum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if sum>ans:
                ans=sum
                lvl=level
        return lvl
                