class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin,end=0,len(nums)-1
        while begin <=end:
            middle=int((begin+end)/2)
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                begin=middle+1
            else:
                end=middle-1
        return -1
                