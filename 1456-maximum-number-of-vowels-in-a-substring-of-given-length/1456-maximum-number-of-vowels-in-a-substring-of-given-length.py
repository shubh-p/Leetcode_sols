class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a=set(['a','e','i','o','u'])
        maxcount,count=-1,0
        for i in range(k):
            if s[i] in a :
                count+=1
        i=0
        maxcount=max(maxcount,count)
        for j in range(k,len(s)):
            if s[i] in a:
                count-=1
            if s[j] in a:
                count+=1
            i+=1
            maxcount=max(maxcount,count)
            if maxcount==k:
                return k
        return maxcount
                