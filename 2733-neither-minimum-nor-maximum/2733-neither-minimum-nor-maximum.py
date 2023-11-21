class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        minn=min(nums[0],nums[1],nums[2])
        maxx=max(nums[0],nums[1],nums[2])
        for num in nums[:3]:
            if num!=minn and num!=maxx:
                return num