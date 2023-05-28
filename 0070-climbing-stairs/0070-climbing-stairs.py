class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def fn(n):
            if n in d:
                return d[n]
            if n==1:
                return 1
            if n==2:
                return 2
            else:
                temp=fn(n-1)+fn(n-2)
                d[n]=temp
                return temp
        return fn(n)