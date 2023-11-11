import heapq

class Graph(object):
    def __init__(self, n, edges):
        self.n_nodes = n
        self.graph   = [[] for _ in range(n)]

        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge):
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1, node2):
        cost  = [float('inf')] * self.n_nodes
        seen  = [False] * self.n_nodes
        queue = [(0, node1)]

        cost[node1] = 0

        while queue:
            c1, v1 = heapq.heappop(queue)
            if not seen[v1]:
                seen[v1] = True
                for v2, c2 in self.graph[v1]:
                    if cost[v2] > c1 + c2:
                        cost[v2] = c1 + c2
                        heapq.heappush(queue, (cost[v2], v2))

        return cost[node2] if cost[node2] < float('inf') else -1