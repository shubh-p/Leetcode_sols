class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans,profit=0,0
        curr=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>curr:
                profit=prices[i]-curr
                curr=prices[i]
                ans+=profit
            elif prices[i]<curr:
                curr=prices[i]
                profit=0
        return ans