class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        a=[0]*201
        #print(a)
        count=0
        for pos,i in enumerate(nums):
            if i>=2*diff:
                count+=a[i-diff] and a[i-2*diff]
            a[i]=1
        return count


            
        