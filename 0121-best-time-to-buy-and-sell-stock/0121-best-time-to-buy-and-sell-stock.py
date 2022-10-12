class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i]-buy > maxSoFar:
                maxSoFar = prices[i]-buy
            buy = min(buy, prices[i])
        return maxSoFar                
                