class Solution:
    def numTrees(self, n: int) -> int:
        memo={}
        def rec(n):
            if n in memo:
                return memo[n]
            if n==0 or n==1:
                return 1
            temp=0
            for i in range(n):
                temp+=rec(i)*rec(n-i-1)
            memo[n]=temp
            return temp
        return rec(n)
        # return memo[n]