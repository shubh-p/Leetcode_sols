class Solution:
    def integerBreak(self, n: int) -> int:
        memo=collections.defaultdict(int,{2:1,3:2,4:4,5:6,6:9})
        def rec(n):
            if n in memo.keys():
                return memo[n]
            else:
                memo[n]=3*rec(n-3)
                return memo[n]
        return rec(n)