class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        a=list(num)
        while a[-1]=='0':
            a.pop()
        return "".join(a)