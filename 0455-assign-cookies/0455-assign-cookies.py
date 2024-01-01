class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=0
        m,n=len(g),len(s)
        ans=0
        for i in range(n):
            if j>=m:
                break
            if s[i]>=g[j]:
                ans+=1
                j+=1
        return ans
