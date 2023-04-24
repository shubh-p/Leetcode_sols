class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        ele=1
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if nums[i] == ele:
                continue
            ele=nums[i]
            target=-1 * ele
            s=i+1
            e=len(nums) - 1
            while(s<e):
                
                if nums[s] + nums[e] == target:
                    ans.add((ele,nums[s],nums[e]))
                    s+=1
                elif nums[s] + nums[e] > target:
                    e-=1
                else:
                    s+=1
        return ans  
            
