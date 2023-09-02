class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        memo=[[-1 for i in range(total+1)]for j in range(n+1)]
        def rec(n,sum):
            if memo[n][sum]!=-1:
                return memo[n][sum]
            if n==0:
                if 2*sum==total:
                    memo[0][sum]=True
                    return True
                else:
                    memo[0][sum]=False
                    return False
            t= rec(n-1,sum+nums[n-1]) or rec(n-1,sum)
            memo[n][sum]=t
            return t
        return rec(n,0)