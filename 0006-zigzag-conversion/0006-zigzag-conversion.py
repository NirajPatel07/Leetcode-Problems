class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        
        res = [[] for _ in range(numRows)]
        row = 0
        sign = 1
        
        for c in s:
            res[row].append(c)
            row += sign
            
            if row == numRows or row == -1:
                sign *= -1
                row += (2*sign)
            
        result = ''
        for char_list in res:
            result += ''.join(char_list)
        
        return result
            