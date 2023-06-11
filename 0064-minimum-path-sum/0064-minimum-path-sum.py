class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            if i == m - 1 and j == n - 1:
                memo[i][j] = grid[i][j]
            elif i == m - 1:
                memo[i][j] = grid[i][j] + dfs(i, j + 1)
            elif j == n - 1:
                memo[i][j] = grid[i][j] + dfs(i + 1, j)
            else:
                right = dfs(i, j + 1)
                down = dfs(i + 1, j)
                memo[i][j] = grid[i][j] + min(right, down)
            return memo[i][j]

        return dfs(0, 0)
