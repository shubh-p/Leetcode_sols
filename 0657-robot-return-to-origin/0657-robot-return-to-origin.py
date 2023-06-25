class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y=0,0
        for c in moves:
            if c == 'U':
                y+=1
            elif c == 'D':
                y-=1
            elif c == 'L':
                x-=1
            else:
                x+=1
        if x == 0  and y == 0:
            return True
        else:
            return False
