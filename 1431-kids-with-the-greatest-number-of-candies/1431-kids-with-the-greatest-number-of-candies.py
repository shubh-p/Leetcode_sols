class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        a=[]
        m-=extraCandies
        for c in candies:
            if c>=m:
                a.append(True)
            else:
                a.append(False)
        return a