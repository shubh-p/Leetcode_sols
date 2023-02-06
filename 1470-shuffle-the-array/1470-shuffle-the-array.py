class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i//2 + i % 2 * (2*n//2)] for i in range(len(nums))]
