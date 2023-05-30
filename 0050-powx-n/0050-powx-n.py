class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        def pow(b,p):
            if p==0:
                return 1
            if p==-1:
                return 1/b
            if p>0:
                if p%2==0:
                    return pow(b*b,p//2)
                else:
                    return b*pow(b*b,p//2)
        ans=pow(x,abs(n))
        if n<0:
            return 1/ans
        else:
            return ans
                    