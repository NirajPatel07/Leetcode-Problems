class Solution(object):
    def minCostConnectPoints(self, points):
        N = len(points)
        adj = {i : [] for i in range(N)}  # i list if [cost,node(neighbour)]
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        #  prims algo
        res=0
        visit = set()
        minheap=[[0,0]]   #[cost,node]
        while len(visit) < N :
            cost,i=heapq.heappop(minheap)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,[neiCost,nei])
        return res