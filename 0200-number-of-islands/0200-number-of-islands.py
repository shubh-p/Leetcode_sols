class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rowlen,collen=len(grid),len(grid[0])
        visited=set()
        islands=0

        def bfs(row,col):
            q=collections.deque()
            q.append((row,col))
            visited.add((row,col))
            while q:
                r,c=q.popleft()
                directions=[[0,1],[1,0],[0,-1],[-1,0]]
                for x,y in directions:
                    nr,nc=r+x,c+y
                    if nr in range(rowlen) and nc in range(collen) and (nr,nc) not in visited and grid[nr][nc]=="1" :
                        q.append((nr,nc))
                        visited.add((nr,nc))
                    
        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands