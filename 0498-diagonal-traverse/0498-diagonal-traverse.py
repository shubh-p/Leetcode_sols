class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        s=m+n-1
        temp={i : [] for i in range(s)}
        ans=[]
        for i in range(m):
            for j in range(n):
                temp[i+j].append(mat[i][j])
        for i in range(s):
            if i%2==0:
                ans+=temp[i][::-1]
            else:
                ans+=temp[i]
        return ans