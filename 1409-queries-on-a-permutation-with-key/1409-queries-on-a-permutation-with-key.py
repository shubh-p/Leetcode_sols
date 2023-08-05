from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        a = deque(range(1, m + 1))
        result = []
        
        for query in queries:
            index = a.index(query)
            result.append(index)
            a.remove(query)
            a.appendleft(query)
        
        return result
