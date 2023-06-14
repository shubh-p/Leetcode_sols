# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def bfs(self,node):
        enc=""
        q=deque()
        q.append(node)
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                if not curr:
                    enc+=","
                    continue
                enc+=str(curr.val) + ","
                q.append(curr.left)
                q.append(curr.right)
        return enc

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        encrypted=self.bfs(root)
        ans=str(encrypted)
        # print(type(ans),ans,encryprt)
        return ans

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        nodes = data.split(",")
        # print(nodes)
        root_val = nodes.pop(0)
        if root_val == "":
            return None
        root = TreeNode(int(root_val))

        queue = deque([root])
        while queue:
            node = queue.popleft()
            left_val = nodes.pop(0)
            if left_val != "":
                node.left = TreeNode(int(left_val))
                queue.append(node.left)
            right_val = nodes.pop(0)
            if right_val != "":
                node.right = TreeNode(int(right_val))
                queue.append(node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))