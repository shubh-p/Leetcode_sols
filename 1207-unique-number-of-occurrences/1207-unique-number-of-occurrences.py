class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        s=set()
        for _ in count.values():
            if _ in s:
                return False
            else:
                s.add(_)
        return True