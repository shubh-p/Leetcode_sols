class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        count,m,i=0,0,0
        while i<len(s):
            x=s[i]
            if x in a:
                m=max(m,count)
                i=a[x]+1
                count=0
                a.clear()
                #a[x]=i
            else:
                a[x]=i
                count+=1
                i+=1
        m=max(count,m)
        return m