class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[first]
        x=first
        for a in encoded:
            x= x ^ a
            ans.append(x)
           # b=x
        return ans
            