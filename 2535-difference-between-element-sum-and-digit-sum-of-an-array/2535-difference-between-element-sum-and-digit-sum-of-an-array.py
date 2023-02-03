class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        ds=0
        for num in nums:
            while(num!=0):
                digit=num%10
                ds+=digit
                num=int(num/10)
        return abs(ds-s)