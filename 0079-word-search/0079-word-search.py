class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # visited=[]
        def rec(index,tofind):
            if len(tofind)==0:
                return True
            up,left,right,down=False,False,False,False
            if board[index[0]+1][index[1]]==tofind[0] and (index[0]+1,index[1]) not in visited:
                visited.append((index[0]+1,index[1]))
                down=rec((index[0]+1,index[1]),tofind[1:])
                visited.pop()

            if board[index[0]-1][index[1]]==tofind[0] and (index[0]-1,index[1]) not in visited:
                visited.append((index[0]-1,index[1]))
                up=rec((index[0]-1,index[1]),tofind[1:])
                visited.pop()

            if board[index[0]][index[1]+1]==tofind[0] and (index[0],index[1]+1) not in visited:
                visited.append((index[0],index[1]+1))
                right=rec((index[0],index[1]+1),tofind[1:])
                visited.pop()

            if board[index[0]][index[1]-1]==tofind[0] and (index[0],index[1]-1) not in visited:
                visited.append((index[0],index[1]-1))
                left=rec((index[0],index[1]-1),tofind[1:])
                visited.pop()
                
            return up or left or right or down
        m,n=len(board),len(board[0])
        for i in range(m):
            board[i].insert(0,"-1")
            board[i].insert(n+1,"-1")
        # buffer=["-1" for i in range]
        board.insert(0,["-1" for i in range(n+2)])
        board.insert(m+1,["-1" for i in range(n+2)])
        # print(board)
        for i in range(m+2):
            for j in range(n+2):
                visited=[]
                if board[i][j]==word[0]:
                    visited.append((i,j))
                    print((i,j))
                    ans=rec((i,j),word[1:])
                    print(visited)
                    print(ans)
                    if ans:
                        return True
        return False

            
