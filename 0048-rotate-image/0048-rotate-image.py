class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """row x becomes n-x-1 column"""

        matrix.reverse()
        print(matrix)
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix