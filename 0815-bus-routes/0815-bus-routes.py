class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = collections.defaultdict(set)
        for i,route in enumerate(routes):
            for r in route:
                graph[r].add(i)
        q = collections.deque()
        
        if graph[source].intersection(graph[target]):
            return 1
        #ids = list(graph[source])
        q.append(source)
        ans = 1
        seen = set()
        while q:
            for _ in range(len(q)):
                r = q.popleft()
                
                idxs = graph[r]
                
                for idx in idxs:
                    if idx in seen:
                        continue
                    for ro in routes[idx]:
                        if ro == target:
                            return ans
                        
                        q.append(ro)
                seen = seen.union(idxs)
            ans += 1
        return -1