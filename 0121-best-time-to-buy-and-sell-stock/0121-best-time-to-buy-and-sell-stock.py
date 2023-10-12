class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            max_profit = max(max_profit, profit)
            if prices[i] < buy:
                buy = prices[i]
        
        return max_profit