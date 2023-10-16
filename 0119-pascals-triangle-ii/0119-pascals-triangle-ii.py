class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(output[i-1][j-1] + output[i-1][j])
            output.append(row)
        
        return output[rowIndex]