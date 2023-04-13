class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a={}
        ans=0
        for num in nums:
            if num in a:
                a[num]+=1
            else:
                a[num]=1
        for ele in a:
            if a[ele]==1:
                ans+=ele


  
        return ans