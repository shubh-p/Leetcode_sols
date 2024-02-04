class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n=len(s),len(t)
        if n>m:
            return ""
        countT=Counter(t)
        window={}
        l=0
        have,need=0,len(countT)
        res,resl=[-1,-1],float('inf')
        for r in range(m):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have+=1
            while need==have:
                if r-l+1 <resl:
                    res=[l,r]
                    resl=r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1

        l,r = res
        return s[l:r+1] if resl!=float('inf') else ""