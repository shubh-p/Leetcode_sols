class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        print(n)
        for i in range(n):
            for j in range(n):
                if i==j:
                    sum+=mat[i][j]
                if i+j==n-1:
                    sum+=mat[i][j]
        if n%2==1:
            sum-=mat[int((n-1)/2)][int((n-1)/2)]
        
        return sum