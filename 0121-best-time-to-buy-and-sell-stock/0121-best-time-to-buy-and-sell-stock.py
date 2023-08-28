class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,ans=0,0
        curr=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>curr:
                profit+=prices[i]-curr
                ans=max(ans,profit)
                curr=prices[i]
            elif prices[i]<curr:
                profit+=prices[i]-curr
                curr=prices[i]
            if profit<1:
                profit=0
        return ans
        