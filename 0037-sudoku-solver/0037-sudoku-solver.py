class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rec(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]==".":
                        for k in range(1,10):
                            if checknum(str(k),i,j):
                                board[i][j]=str(k)
                                if rec(board) == True:
                                    return True
                                else:
                                    board[i][j]="."
                        return False
            return True               
                        
        def checknum(num,row,col):
            if num in board[row]:
                return False
            if num in [board[i][col] for i in range(9)]:
                return False
            box_row_start = 3 * (row // 3)
            box_col_start = 3 * (col // 3)
            if num in [board[i][j] for i in range(box_row_start,box_row_start+3) for j in range(box_col_start,box_col_start+3)]:
                       return False
            return True
        rec(board)
                       