class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Return input if numRows is 1
        if numRows == 1:
            return s
        
        # Store each row of zigzag pattern
        zigzagRows = ["" for i in range(numRows)]
        
        # Keep track of current row and direction
        row, direction = 0, 1
        
        # Iterate through input string characters
        for ch in s:
            # Add character to corresponding row
            zigzagRows[row] += ch
            
            # Change direction at last or first row
            if row == numRows-1:
                direction = -1
            if row == 0:
                direction = 1
                
            # Update row based on direction
            row += direction
        
        # Join and return zigzagRows as a string
        return "".join(zigzagRows)