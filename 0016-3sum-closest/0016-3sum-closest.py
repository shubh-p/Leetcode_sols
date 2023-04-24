class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        if len(nums)==3:
            return sum(nums)
        ans=10**5
        toprint=-1
        nums.sort()
        for i,x in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=x+nums[l]+nums[r]
                diff=abs(target-s)
                if diff<ans:
                    ans=diff
                    toprint=s
                if s>target:
                    r-=1
                elif s<target:
                    l+=1
                else:
                    break
                    #-4,-1,1,2
        return toprint
                
                    