class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        return (len(a) != len(nums))