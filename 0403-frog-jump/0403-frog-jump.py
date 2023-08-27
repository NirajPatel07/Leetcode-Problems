class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dp(i, k):
            if i == len(stones) - 1: return True
            
            for jump in range(k - 1, k + 2):
                j = bin_search(i + 1, stones[i] + jump)

                if j != -1 and dp(j, jump): return True

            return False

        def bin_search(start, x):
            l, r = start, len(stones) - 1

            while l <= r:
                m = (l + r) // 2

                if stones[m] == x: return m

                if stones[m] > x:
                    r = m - 1
                else:
                    l = m + 1

            return -1

        return dp(0, 0)