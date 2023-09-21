class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        a=set()
        for to in edges:
            a.add(to[1])
        b=set([i for i in range(n)])
        return b.difference(a)
