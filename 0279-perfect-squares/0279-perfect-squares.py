class Solution:
    def numSquares(self, n: int) -> int:
        
        dp={}
        def rec(n,sol):
            if n in dp:
                return dp[n]
            if n==0:
                return 0
            for i in range(1,int(sqrt(n))+1,1):
                ans = rec(n-i**2,sol) +1
                if ans<sol:
                    sol=ans
            dp[n]=sol
            return sol
        
        return rec(n,float('inf'))