class Solution:
    def maxCoins(self, piles):
        piles.sort()
        ans=0
        n=len(piles)
        for i in range(1,(n//3)+1):
            ans+=piles[n-(2*i)]
        return ans
