class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxp=[]
        ans=max(nums)
        maxproduct,minproduct=1,1
        for num in nums:
            temp=maxproduct*num
            maxproduct=max(maxproduct*num,minproduct*num,num)
            minproduct=min(temp,minproduct*num,num)
            print(maxproduct,minproduct)
            ans=max(maxproduct,ans)
        return ans