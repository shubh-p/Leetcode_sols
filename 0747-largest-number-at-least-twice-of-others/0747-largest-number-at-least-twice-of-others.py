class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1,max2,pos=nums[0],-1,0
        for i in range(1,len(nums)):
            if nums[i]>max1:
                max2=max1
                max1=nums[i]
                pos=i
            elif nums[i]>max2:
                max2=nums[i]
        #print(max1,max2,pos)
        if max1>=2*max2:
            return pos
        else:
            return -1
            
            
        