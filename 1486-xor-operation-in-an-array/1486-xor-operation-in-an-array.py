class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        nums = [start + n * 2 for n in range(n)]
        
        for n in nums:
            ans = ans ^ n
        return ans 
        