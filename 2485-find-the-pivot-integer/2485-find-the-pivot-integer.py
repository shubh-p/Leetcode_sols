class Solution:
    def pivotInteger(self, n: int) -> int:
        ans=sqrt((n*(n+1))/2)
        #print(int(ans)==ans)
        if int(ans)!=ans:
            return -1
        return int(ans)
        