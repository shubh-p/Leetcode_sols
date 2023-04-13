# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def search(node1: TreeNode, node2: TreeNode, target: TreeNode) -> TreeNode:
            if not node1:
                return None
            if node1 == target:
                return node2
            left_result = search(node1.left, node2.left, target)
            if left_result:
                return left_result
            return search(node1.right, node2.right, target)
        
        return search(original, cloned, target)
