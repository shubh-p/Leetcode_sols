# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node.left:
                return -1
            if node.left.val==node.right.val:
                left=rec(node.left)
                right=rec(node.right)
                if left==-1 and right==-1:
                    return -1
                elif left==-1 or right==-1:
                    return max(left,right)
                else:
                    return min(left,right)
            else:
                if node.left.val==node.val:
                    right=node.right.val
                    left=rec(node.left)
                else:
                    left=node.left.val
                    right=rec(node.right)
                if left==-1 or right==-1:
                    return max(left,right)
                else:
                    return min(left,right)
        return rec(root)
        