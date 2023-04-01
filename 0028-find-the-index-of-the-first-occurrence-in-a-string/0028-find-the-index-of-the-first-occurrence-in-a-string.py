class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        n=len(haystack)
        m=len(needle)
        lps=[0]*m
        prevlps,i=0,1
        while i<m:
            if needle[i]==needle[prevlps]:
                lps[i]=prevlps+1
                i+=1
                prevlps+=1
            elif prevlps==0:
                lps[i]=0
                i+=1
            else:
                prevlps=lps[prevlps-1]
        i,j=0,0
        while i<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
            if j==m:
                return i-m
        return -1