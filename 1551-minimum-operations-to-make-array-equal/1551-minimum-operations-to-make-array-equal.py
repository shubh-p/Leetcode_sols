class Solution:
    def minOperations(self, n: int) -> int:
        if n%2==0:
            return (n*n)//4
        else:
            return int((n//2)/2*(n+1))