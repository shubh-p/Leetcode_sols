class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            print(c,t)
            if c in t:
                index=t.index(c)
                t=t[index+1:]
            else:
                return False
        return True