class Solution(object):
    def minEatingSpeed(self, piles, h):
        low, high = 1, 10 ** 9
        while low <= high:
            k = (low + high) // 2
            if sum(math.ceil(1.0 * pile / k) for pile in piles) > h: low = k + 1
            else: high = k - 1
        return low