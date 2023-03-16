class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n-1] * nums[n-2] - nums[0] * nums[1]
        