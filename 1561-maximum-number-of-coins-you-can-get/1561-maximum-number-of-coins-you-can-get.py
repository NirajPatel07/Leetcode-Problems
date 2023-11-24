class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        rounds = len(piles) // 3
        idx = rounds
        result = 0
        
        for _ in range(rounds):
            result += piles[idx]
            idx += 2
        
        return result