class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n_r = len(grid)
        n_c = len(grid[0])
        answer = list(range(n_c))
        
        for r in range(n_r):
            for i in range(n_c):
                c = answer[i]
                if c == -1: continue
                c_nxt = c + grid[r][c]
                if c_nxt < 0 or c_nxt >= n_c or grid[r][c_nxt] == -grid[r][c]:
                    answer[i] = -1
                    continue
                answer[i] += grid[r][c]
        
        return answer
                