class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,x in enumerate(nums):
            tofind=target-x
            if tofind in a:
                return [a[tofind],i]
            a[x]=i;
        return []
        