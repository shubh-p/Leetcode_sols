class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cl,cr,ans=0,0,0
        for c in s:
            if cl==cr and cl!=0:
                ans+=1
                cl,cr=0,0
            if c=='L':
                cl+=1
            elif c=='R':
                cr+=1
        return ans+1