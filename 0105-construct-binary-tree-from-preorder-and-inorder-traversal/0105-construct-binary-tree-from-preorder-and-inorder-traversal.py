# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  
        map={v:i for i,v in enumerate(inorder)}
        def fn(i,j):
            if i==j:
                return None
            val=preorder.pop(0)
            pos=map[val]
            root=TreeNode(val)
            root.left=fn(i,pos)
            root.right=fn(pos+1,j)
            return root
        return fn(0,len(inorder))
        