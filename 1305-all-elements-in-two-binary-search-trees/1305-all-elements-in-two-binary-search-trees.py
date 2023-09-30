# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node):
            if not node:
                return []
            leftval=inorder(node.left)
            rightval=inorder(node.right)
            return leftval + [node.val] + rightval
        a=inorder(root1)
        b=inorder(root2)
        print(a,b)
        ans=[]
        n1=len(a)
        n2=len(b)
        i,j=0,0
        while i<n1 or j<n2:
            if i==n1:
                ans+=b[j:]
                break
            if j==n2:
                ans +=a[i:]
                break
            if a[i]<b[j]:
                ans.append(a[i])
                i+=1
            else:
                ans.append(b[j])
                j+=1
        
        return ans


            