class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ans=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                ans=min(ans,nums[l])
                break
            mid=(l+r)//2
            ans=min(ans,nums[mid])
            
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
            
        return ans