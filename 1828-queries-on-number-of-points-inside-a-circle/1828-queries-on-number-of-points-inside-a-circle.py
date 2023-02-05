class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def distance(x1:int,y1: int,x2:int, y2:int) ->int:
            return (x2-x1)**2+(y2-y1)**2
        ans=[]
        for circle in queries:
            sum=0
            for point in points:
                if distance(circle[0],circle[1],point[0],point[1]) <= circle[2]**2:
                    sum+=1
            ans.append(sum)
        return ans

                