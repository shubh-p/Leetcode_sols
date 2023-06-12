# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def fn(arr):
            if not arr:
                return None
            val=postorder.pop()
            pos=arr.index(val)
            root=TreeNode(val)
            root.right=fn(arr[pos+1:])
            root.left=fn(arr[0:pos])
            return root

        return fn(inorder)