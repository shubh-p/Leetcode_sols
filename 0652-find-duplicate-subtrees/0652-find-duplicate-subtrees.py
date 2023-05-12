# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees=defaultdict(list)
        res=[]
        def preorder(root):
            if not root:
                return "X"
            s=",".join([str(root.val),preorder(root.left),preorder(root.right)])
            if len(subtrees[s])==1:
                res.append(root)
            subtrees[s].append(root)
            return s
        
        preorder(root)
        return res