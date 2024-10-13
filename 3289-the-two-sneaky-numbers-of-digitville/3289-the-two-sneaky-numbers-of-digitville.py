class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        ans=[]
        for num in nums:
            if num in s:
                ans.append(num)
            else:
                s.add(num)
            if len(ans)==2:
                return ans