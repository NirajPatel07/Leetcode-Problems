class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
    ) -> bool:
        adj_map = {}
        visited = []
        if n == 1:
            return True

        for n1, n2 in edges:
            if n1 not in adj_map:
                adj_map[n1] = []
            if n2 not in adj_map:
                adj_map[n2] = []

            adj_map[n1].append(n2)
            adj_map[n2].append(n1)

        _Q = [source]

        while _Q:
            _n = _Q.pop(0)  # Get current node for BFS
            if _n in visited or _n not in adj_map:  # if already visited, pass
                continue
            visited.append(_n)  # if not already visited, add to visited
            if destination in adj_map[_n]:  # True, if destination is connected
                return True
            else:  # Else add children to _Q.
                _Q.extend(adj_map[_n])

        return False