class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1 and self.isSpecial(mat, r, c):
                    count += 1
        
        return count
    
    def isSpecial(self, mat, row, column):
        rowData = mat[row]
        if rowData.count(1) > 1:
            return False
        
        upRow, downROw = row, row
        while upRow-1 >= 0:
            upRow -= 1
            if mat[upRow][column] != 0:
                return False
        
        while downROw+1 < len(mat):
            downROw += 1
            if mat[downROw][column] != 0:
                return False
        
        return True
        
        