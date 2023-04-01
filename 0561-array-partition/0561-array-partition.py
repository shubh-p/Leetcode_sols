class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum=0
        for i,a in enumerate(nums):
            if i%2==0:
                sum+=a
        return sum