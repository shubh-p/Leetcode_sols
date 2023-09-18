class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        ans=[]
        m=len(s)
        for i in range(m):
            x,y=startPos
            count=0
            for c in s:
                if c is "R":
                    y+=1
                elif c is "L":
                    y-=1
                elif c is "D":
                    x+=1
                else:
                    x-=1
                if x>=n or y>= n or x<0 or y<0:
                    break
                count+=1
            # print(x,y,s,count)
            ans.append(count)
            s=s[1:]
        return ans