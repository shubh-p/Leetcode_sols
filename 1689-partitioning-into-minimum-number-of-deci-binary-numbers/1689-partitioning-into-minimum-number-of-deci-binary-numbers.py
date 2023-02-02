class Solution:
    def minPartitions(self, n: str) -> int:
        m=-1
        for c in n:
            m=max(m,int(c))
        return m
        