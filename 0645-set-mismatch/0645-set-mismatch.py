class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0 for i in range(1,n+1)]
        for num in nums:
            arr[num-1]+=1
        a,b=0,0
        for idx,count in enumerate(arr):
            if count==0:
                b=idx+1
            if count==2:
                a=idx+1
        return [a,b]