class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, val):
            if not node:
                return None
            if node.val == val:
                if not node.left and not node.right:
                    return None
                if not node.left and node.right:
                    return node.right
                if not node.right and node.left:
                    return node.left
                if node.left and node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    node.val = temp.val
                    node.right = delete(node.right, temp.val)
            
            elif node.val > val:
                node.left = delete(node.left, val)
            else:
                node.right = delete(node.right, val)

            return node

        return delete(root, key)
