class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        s=0
        for i in nums:
            s+=i
        left,right=0,s-nums[0]
        for i in range(len(nums)-1):
            #print(left,right)
            if left==right:
                return i
            left+=nums[i]
            right-=nums[i+1]
        if left==right:
            return i+1
        return -1