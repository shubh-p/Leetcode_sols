class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a=[0 for i in range(26)]
        ans=0
        for i in range(len(s)):
            a[ord(s[i])-ord('a')]+=i
            a[ord(t[i])-ord('a')]-=i
        for num in a:
            ans+=abs(num)
        return ans
              