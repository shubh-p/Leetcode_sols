import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mrow=[]
        mcol=[]
        m=0
        sum=0
        arr=np.array(grid)
        arr=arr.transpose()
        print(arr)
        for row in grid:
            mrow.append(max(row))
        for col in arr:
            mcol.append(max(col))
        print(mrow,mcol)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                m=min(mrow[i],mcol[j])
                if grid[i][j]<m:
                    sum+=m-grid[i][j]
        return sum
