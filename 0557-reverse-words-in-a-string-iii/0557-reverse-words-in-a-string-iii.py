class Solution:
    def reverseWords(self, s: str) -> str:
        word=""
        ans=""
        for c in s:
            if c == ' ':
                ans+=word[::-1]
                ans+=" "
                word=""
            else:
                word+=c
        if s[len(s)-1] != ' ':
            ans+=word[::-1]
        return ans