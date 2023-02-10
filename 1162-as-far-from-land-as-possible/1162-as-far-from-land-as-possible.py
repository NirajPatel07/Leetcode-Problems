class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        bfs_queue = [] # queue for breadth-first search
        visited = [[False for i in range(n)] for j in range(n)] 
        
        # initialize bfs_queue with all the land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs_queue.append((i,j,0))
                    visited[i][j] = True
        
        max_distance = 0
        while bfs_queue:
            row, col, distance = bfs_queue.pop(0)
            if grid[row][col] == 0 : max_distance = max(max_distance, distance)
            # add unvisited neighbors to the bfs_queue
            for x, y in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = True
                    bfs_queue.append((x, y, distance + 1))
        
        return max_distance if max_distance != 0 else -1
