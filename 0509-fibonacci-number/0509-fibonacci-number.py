class Solution:
    def fib(self, n: int) -> int:
        memo={}
        def rec(n):
            if n in memo:
                return memo[n]
            if n==0 or n==1:
                return n
            res=rec(n-1)+rec(n-2)
            memo[n]=res
            return res
        return rec(n)