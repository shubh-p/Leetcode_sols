class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return max(nums)
        ans=0
        dp=[[-1 for j in range(sum(nums)+1)] for i in range(len(nums))]
        def rec(idx,s):
            if idx>=n:
                return s
            if dp[idx][s]!=-1:
                return dp[idx][s]
            nonlocal ans
            for i in range(idx,n):
                ans=max(ans,rec(i+2,s+nums[i]))
            dp[idx][s]=ans
            return ans
        a=rec(2,nums[0])
        ans=0
        b=rec(3,nums[1])
        return max(a,b)
            
            