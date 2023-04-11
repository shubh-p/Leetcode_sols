class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m,alt=0,0
        for h in gain:
            alt+=h
            if alt>m:
                m=alt
        return m