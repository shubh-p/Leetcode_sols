# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.ans=[]
        self.dic={}
        self.ptr=-1
        self.obj=root
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)
        dfs(root)
        self.dic={i:v for i,v in enumerate(self.ans)}
        # print(self.ans)
    def next(self) -> int:
        self.ptr+=1
        return self.dic[self.ptr]

    def hasNext(self) -> bool:
        if self.ptr<len(self.ans)-1:
            return True
        else:
            return False
    # del ans
    # del dic
    # del ptr
    # del obj

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()