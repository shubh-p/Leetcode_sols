class Solution:
    def firstUniqChar(self, s: str) -> int:
        a={}
        for i in s:
            a[i]=a.get(i,0)+1
        for i,x in enumerate(s):
            if a[x]==1:
                return i
        return -1