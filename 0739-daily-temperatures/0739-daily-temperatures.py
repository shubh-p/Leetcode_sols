class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[-1 for i in range(len(temperatures))]
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            curr=temperatures[i]
            while len(stack)>0 and stack[-1][0] <=curr:
                    stack.pop(-1)
            if len(stack)==0:
                stack.append((curr,i))
                ans[i]=0
            else:
                ans[i]=stack[-1][1]-i
                stack.append((curr,i))
        return ans
                
            