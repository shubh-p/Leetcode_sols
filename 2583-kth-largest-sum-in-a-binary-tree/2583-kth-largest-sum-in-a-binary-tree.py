# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=deque()
        dic=[]
        lvl=0
        q.append(root)
        while q:
            lvl+=1
            sum=0
            for i in range(len(q)):
                curr=q.popleft()
                sum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            dic.append(sum)
            
        # print(dic)
        if len(dic)<k:
            return -1
        dic.sort(reverse=True)
        # print(dic)
        return dic[k-1]
            