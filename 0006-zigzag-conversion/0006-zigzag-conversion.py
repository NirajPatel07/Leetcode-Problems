class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        
        res = [[] for _ in range(numRows)]
        row = 0
        step = 1
        
        for c in s:
            res[row].append(c)
            row += step
            if row == numRows or row < 0:
                step *= -1
                row += (step * 2)
                
        result = ''
        
        for row in res:
            result += ''.join(row)
            
        return result
        
        