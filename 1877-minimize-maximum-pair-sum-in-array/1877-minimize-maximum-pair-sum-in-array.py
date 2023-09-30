class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        ans=-1
        while i<j:
            ans=max(ans,nums[i]+nums[j])
            i+=1
            j-=1
        return ans