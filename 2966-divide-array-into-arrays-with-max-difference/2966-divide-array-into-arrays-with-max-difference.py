class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort(reverse=True)
        idx=0
        ans=[]
        while idx<len(nums):
            row=[]
            row.append(nums[idx])
            maxx=row[-1]
            for i in range(1,3):
                diff=maxx-nums[idx+i]
                if diff<=k:
                    row.append(nums[idx+i])
                else:
                    return []
            ans.append(row)
            idx+=3     
        return ans
            