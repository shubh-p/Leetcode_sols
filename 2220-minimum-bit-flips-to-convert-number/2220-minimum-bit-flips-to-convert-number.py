class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=start ^ goal
        count=0
        for i in bin(a):
            if i == '1':
                count+=1
        return count