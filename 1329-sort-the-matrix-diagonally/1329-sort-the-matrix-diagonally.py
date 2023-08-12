class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        diagonals=[[] for i in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                # print(i-j)
                diagonals[i-j+n-1].append(mat[i][j])
        
        for i in range(m+n-1):
            diagonals[i].sort(reverse=True)
        print(diagonals)
        for i in range(m):
            for j in range(n):
                mat[i][j]=diagonals[i-j+n-1].pop()
            
        return mat