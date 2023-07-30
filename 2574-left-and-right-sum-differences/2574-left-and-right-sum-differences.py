class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightsum=sum(nums)
        leftsum=0
        ans=[]
        for i in range(len(nums)):
            curr=nums[i]
            ans.append(abs(rightsum-leftsum-curr))
            rightsum-=curr
            leftsum+=curr
        return ans