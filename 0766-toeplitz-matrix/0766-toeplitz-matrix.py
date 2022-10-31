class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]])->bool:
        # Initialise Row lenght and Column length
        r_len, c_len = len(matrix),len(matrix[0])
        
        # For every row
        for r in range (1, r_len):
            # For every column
            for c in range (1, c_len):
                # Check if diagonal element are equal or not
                if matrix[r][c]!=matrix[r-1][c-1]:
                    # If diagonal elements are not equal then return False
                    return False
        
        # If for loop is executed it means it satify the condition. Return True
        return True