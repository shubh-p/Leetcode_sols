class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        column, ndiag, pdiag = set(), set(), set()
        
        def rec(row):
            if row == n:
                ans.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col not in column and row-col not in ndiag and row+col not in pdiag:
                    board[row][col] = 'Q'
                    column.add(col)
                    pdiag.add(row+col)
                    ndiag.add(row-col)
                    rec(row + 1)
                    column.remove(col)
                    pdiag.remove(row+col)
                    ndiag.remove(row-col)
                    board[row][col] = '.'
        
        rec(0)
        return ans
