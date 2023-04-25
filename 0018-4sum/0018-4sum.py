class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        ans=set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]==target:
                        ans.add(tuple([nums[i],nums[j],nums[l],nums[r]]))
                        l+=1
                    elif nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
                    else:
                        l+=1
        return ans


