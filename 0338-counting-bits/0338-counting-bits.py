class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0 for i in range(n+1)]
        # dp[0]=0
        offset=1
        for i in range(1,n+1):
            if offset*2==i:
                offset*=2
            dp[i]=1+dp[i-offset]
        return dp
