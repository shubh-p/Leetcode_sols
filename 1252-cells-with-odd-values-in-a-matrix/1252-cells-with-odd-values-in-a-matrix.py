class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat=[[0]*n for i in range(m)] 
        #print(mat)
        count=0
        for indice in indices:
            for j in range(m):
                mat[j][indice[1]]+=1
            for j in range(n):
                mat[indice[0]][j]+=1
            #print(mat)
        #print(mat)
        for i in range(m):
            for j in range(n):
                if mat[i][j]%2==1:
                    count+=1       
        return count