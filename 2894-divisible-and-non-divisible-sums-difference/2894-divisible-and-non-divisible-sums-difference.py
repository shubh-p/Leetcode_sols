class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return int((n*(n+1)/2)-(m*(n//m)*((n//m)+1)))