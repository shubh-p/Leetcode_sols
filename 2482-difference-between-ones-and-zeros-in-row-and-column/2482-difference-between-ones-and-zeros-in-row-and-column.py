class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total=m+n
        for i in range(m):
            grid[i].append(0)
        grid.append([0 for i in range(len(grid[0]))])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][n]+=1
                    grid[m][j]+=1
        for i in range(m):
            for j in range(n):
                grid[i][j]=2*(grid[i][n]+grid[m][j])-total
        
        print(grid)
        for i in range(m):
            grid[i].pop()
        grid.pop()

        return grid
        