class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zigzagRows =  ["" for i in range(numRows)]
        
        row, i = 0, 1
        
        for ch in s:
            zigzagRows[row] += ch
            
            if row == numRows-1:
                i = -1
            
            if row == 0:
                i = 1
                
            row += i
        
        return "".join(zigzagRows)