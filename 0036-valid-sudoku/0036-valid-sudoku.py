class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seta=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                elea=board[i][j]
                eleb=board[j][i]
                if elea!=".":
                    ele1=elea+"row"+str(i)
                    if ele1 in seta:
                        return False
                    else:
                        seta.add(ele1)
                    ele2=str(elea)+"mat"+str((i+3)//3)+str((j+3)//3)
                    if ele2 in seta:
                        return False
                    else:
                        seta.add(ele2)
                if eleb!=".":
                    ele3=eleb+"col"+str(i)
                    if ele3 in seta:
                        return False
                    else:
                        seta.add(ele3)     
        return True