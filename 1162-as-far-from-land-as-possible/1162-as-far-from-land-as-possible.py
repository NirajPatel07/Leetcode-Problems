class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        vist = [[False for i in range(n)] for j in range(n)] 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    vist[i][j] = True
        ans = 0
        while queue:
            r,c,d = queue.pop(0)
            if grid[r][c] == 0 :ans = max(ans,d)
            for x,y in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0 <= x < n and 0 <= y < n and vist[x][y] == False:
                    vist[x][y] = True
                    queue.append((x,y,d+1))
        return ans if ans != 0 else -1