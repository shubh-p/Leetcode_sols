class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while(l<r):
            if(nums[l]%2==1):
                if(nums[r]%2==0):
                    nums[l], nums[r]=nums[r], nums[l]
                    l+=1
                    r-=1
                else: r-=1
            else: l+=1
        return nums