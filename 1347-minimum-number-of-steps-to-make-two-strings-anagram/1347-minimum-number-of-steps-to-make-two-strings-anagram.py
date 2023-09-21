class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic={}
        ans=0
        for c in t:
            dic[c]=dic.get(c,0)+1
        for c in s:
            if c in dic:
                dic[c]-=1
        for c in dic:
            if dic[c]>0:
                ans+=dic[c]
        
        return ans
        
        