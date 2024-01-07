class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n)]
        # print(dp)
        ans=0
        for i in range(n):
            # print(i)
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=dp[j][diff] + 1
                ans+=dp[j][diff] + 1
        # print(ans)
        # print(dp)
        return ans-(n*(n-1)//2)