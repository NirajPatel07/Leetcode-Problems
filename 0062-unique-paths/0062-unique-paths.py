class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        
        def path_explorer(row, column):
            if row == 1 and column == 1:
                return 1
            
            if row == 0 or column == 0:
                return 0
            
            if dp[row][column] != -1:
                return dp[row][column]
            
            dp[row][column] = path_explorer(row-1, column) + path_explorer(row, column-1)
            
            return dp[row][column]
        
        result = path_explorer(m, n)
        
        return result