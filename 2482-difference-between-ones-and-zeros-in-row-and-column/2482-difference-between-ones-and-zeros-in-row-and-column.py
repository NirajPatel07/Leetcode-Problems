class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        rowZeros, columnZeros, rowOnes, columnOnes = self.gridDifference(grid)
        
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                matrix[row][column] = rowOnes[row] + columnOnes[column] - rowZeros[row] - columnZeros[column]
        
        return matrix
    
    def gridDifference(self, grid):
        rowZeros = []
        columnZeros = []
        rowOnes = []
        columnOnes = []
        
        for row in range(len(grid)):
            rowZeros.append(grid[row].count(0))
            rowOnes.append(grid[row].count(1))
        
        for column in range(len(grid[0])):
            
            zeroCount, oneCount = 0, 0
            for row in range(len(grid)):
                if grid[row][column] == 1:
                    oneCount += 1
                else:
                    zeroCount += 1
                    
            columnZeros.append(zeroCount)
            columnOnes.append(oneCount)
        
        return rowZeros, columnZeros, rowOnes, columnOnes