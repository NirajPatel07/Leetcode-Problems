from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        G = defaultdict(list)
        for v, w in roads:
            G[v].append(w)
            G[w].append(v)
        ans = 0
        visited = set()
        def dfs(v):
            nonlocal ans
            if v in visited: return 0
            visited.add(v)
            res = 0
            for w in G[v]:
                cur = dfs(w)
                ans += (cur + seats - 1) // seats
                res += cur
            return res + 1
        dfs(0)
        return ans