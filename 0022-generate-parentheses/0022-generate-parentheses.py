class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def rec(s,o,c):
            if o==0 and c==0:
                ans.append(s)
                return 
            if o>0:
                s1=s+"("
                rec(s1,o-1,c)
            if c>o:
                s2=s+")"
                rec(s2,o,c-1)        
        rec("(",n-1,n)
        return ans