class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xpts=[]
        for pair in points:
            xpts.append(pair[0])
        print(xpts)
        xpts.sort()
        ans,diff=0,0
        for i in range(1,len(xpts)):
            diff=xpts[i]-xpts[i-1]
            ans=max(ans,diff)
        return ans