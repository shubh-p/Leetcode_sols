class Solution:
    def replaceDigits(self, s: str) -> str:
        for i,x in enumerate(s):
            if i%2==1:
                s=s.replace(x,chr(ord(s[i-1])+int(x)),1)
        return s