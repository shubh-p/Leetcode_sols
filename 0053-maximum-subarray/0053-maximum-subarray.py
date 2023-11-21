class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float('-inf')
        maxtillnow=0
        for i in range(len(nums)):
            maxtillnow+=nums[i]
            if maxtillnow>ans:
                ans=maxtillnow
            if maxtillnow<0:
                maxtillnow=0
        return ans