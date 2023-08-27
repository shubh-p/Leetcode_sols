class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        stack.append((-1,-1))
        ans=-1
        n=len(heights)
        for i,height in enumerate(heights):
            if height>stack[-1][1]:
                stack.append((i,height))
            elif height<stack[-1][1]:
                    while height<stack[-1][1]:
                        start,towerheight=stack.pop()
                        width=i-start
                        area=width*towerheight
                        ans=max(ans,area)
                    stack.append((start,height))
        while stack:
            start,towerheight=stack.pop()
            if start==-1:
                return ans
            width=n-start
            area=width*towerheight
            ans=max(ans,area)
        return ans

            