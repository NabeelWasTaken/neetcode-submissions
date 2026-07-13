class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l = 0
        maxProfit = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            
            profit = (prices[r] - prices[l])
            maxProfit = max(profit, maxProfit)

        
        return maxProfit
            
        