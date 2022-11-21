class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS solution
        import collections
        m,n = len(maze), len(maze[0])

        dirs = [(0,1), (0,-1), (1,0), (-1,0)] # Directions to search
        q = collections.deque([(entrance[0], entrance[1], 0)]) # Start with adding entry point to the queue

        while(q):
            x,y, dist = q.popleft() # Check each element in the order it was added to the queue
            for dir in dirs:
                new_x, new_y = x+dir[0], y+dir[1]

                # Out of bounds or hitting the wall case
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or maze[new_x][new_y] == '+': 
                    continue

                # If the new point is not the entry point and if the new point is the boundary element and the new point is empty, we have found our solution.
                if (new_x != entrance[0] or new_y != entrance[1]) and (new_x == 0 or new_y == 0 or new_x == m-1 or new_y == n-1) and (maze[new_x][new_y] == '.'):
                    return dist+1
                
                # Mark the new point as visited (or make it a wall.)
                maze[new_x][new_y] = '+'

                # Add new point to the queue for searching
                q.append((new_x, new_y, dist+1))

        return -1