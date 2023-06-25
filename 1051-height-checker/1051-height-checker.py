class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=[0]*101
        for i in heights:
            count[i]+=1
        sol=0
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        print(count)
        ans=[0]*len(heights)
        for i in heights:
            ans[count[i]-1]=i
            count[i]-=1
        for i in range(len(heights)):
            if ans[i]!=heights[i]:
                sol+=1
        return sol

        