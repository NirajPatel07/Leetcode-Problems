class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left_over = money - prices[0] - prices[1]
        if left_over >= 0:
            return left_over
        else:
            return money