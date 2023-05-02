class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                prod*=-1
        return prod
                