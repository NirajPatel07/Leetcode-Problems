class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        
        while right < len(prices):
            currProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxProfit = max(currProfit, maxProfit)
            else:
                left = right
            right+=1
        
        return maxProfit
                