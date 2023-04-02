class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j,sum,ans,flag=0,0,0,len(nums),False
        while i<len(nums) and j<len(nums):
            sum+=nums[j]
            if sum>=target:
                while sum>=target:
                    ans=min(ans,j+1-i)
                    flag=True
                    sum-=nums[i]
                    i+=1         
            j+=1
        if flag:
            return ans
        else:
            return 0