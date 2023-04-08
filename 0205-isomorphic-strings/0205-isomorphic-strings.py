class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        a={}
        for i in range(n):
            if s[i] in a:
                if a[s[i]]!=t[i]:
                    return False
            else:
                if t[i]in a.values():
                    return False
                a[s[i]]=t[i]
        return True

