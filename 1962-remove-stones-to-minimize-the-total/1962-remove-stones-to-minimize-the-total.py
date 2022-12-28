class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pile = [ -i for i in piles]
        heapq.heapify(pile)
        while k:
            pop = heapq.heappop(pile)//2
            heapq.heappush(pile,pop)
            k -= 1
        return -(sum(pile))