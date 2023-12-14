class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid[0]), len(grid)
        n_m = n + m
        
        csums2 = tuple(c.count(1) * 2 for c in zip(*grid))

        for i in range(m):
            rsums2_nm = grid[i].count(1) * 2 - n_m
            
            for j in range(n):
                grid[i][j] = rsums2_nm + csums2[j]

        return grid