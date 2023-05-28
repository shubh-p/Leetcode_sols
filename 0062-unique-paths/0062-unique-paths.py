class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def fact(n):
            if n in memo:
                return memo[n]
            if n==0:
                return 1
            temp=fact(n-1)*n
            memo[n]=temp
            return temp
        a=fact(m+n-2)
        b=fact(m-1)
        c=fact(n-1)
        ans=a/(b*c)
        return int(ans)  