class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def rec(i):
            if dp[i]!=-1:
                return dp[i]
            if i==0 or i==1:
                dp[i]=cost[i]
                return cost[i]
            dp[i]=  min(cost[i]+rec(i-1),cost[i]+rec(i-2))
            return dp[i]
        cost.append(0)
        dp=[-1 for i in range(len(cost))]
        return rec(len(cost)-1)