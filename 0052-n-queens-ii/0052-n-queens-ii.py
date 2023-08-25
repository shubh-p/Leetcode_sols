class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        column,pdiag,ndiag=set(),set(),set()
        
        def rec(row):
            if row==n:
                nonlocal count
                count+=1
                return
            for col in range(n):
                if col not in column and row+col not in pdiag and row-col not in ndiag:
                    column.add(col)
                    pdiag.add(row+col)
                    ndiag.add(row-col)
                    rec(row+1)
                    column.remove(col)
                    pdiag.remove(row+col)
                    ndiag.remove(row-col)
                    
        rec(0)
        return count