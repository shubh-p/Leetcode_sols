class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a={}
        count=0
        for c in stones:
            a[c] = 1 + a.get(c,0)
        for j in jewels:
            if j in a.keys():
                count+=a[j]
        return count
        