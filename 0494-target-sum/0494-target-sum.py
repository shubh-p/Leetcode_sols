class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        total=sum(nums)
        sums=(total+target)//2
        if total < target or target<-1*(total) or (total + target) % 2 != 0:
            return 0
        dp=[[0 for j in range(sums+1)]for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        
        for i in range(1,n+1):
            for j in range(1,sums+1):
                if nums[i-1]>j or nums[i-1]==0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return 2**(nums.count(0))*dp[n][sums]

        