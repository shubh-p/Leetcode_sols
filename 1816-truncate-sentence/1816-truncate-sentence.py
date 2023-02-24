class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a=list(s.split(" "))
        print(a)
        ans=""
        for word in a:
            ans+=word
            if k>1:
                ans+=" "
            k-=1
            if k == 0:
                break
        return ans