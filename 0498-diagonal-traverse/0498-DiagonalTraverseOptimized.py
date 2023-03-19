class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        ans=[]
        #print(m,n,len(ans))
        r,c=0,0
        for i in range(m*n):
            ans.append(mat[r][c])
            if (r+c)%2==0:
                if c==n-1:
                    r+=1
                elif r==0:
                    c+=1
                else:
                    r-=1
                    c+=1
            else:
                if r==m-1:
                    c+=1
                elif c==0:
                    r+=1
                else:
                    r+=1
                    c-=1
        return ans
        
