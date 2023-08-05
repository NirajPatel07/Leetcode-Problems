class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit, profit = prices[0], 0
        
        for i in range(len(prices)):
            if min_profit > prices[i]:
                min_profit, max_profit = prices[i], prices[i]
            profit = max(profit, prices[i]-min_profit)
            
        return profit