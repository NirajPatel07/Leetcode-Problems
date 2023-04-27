class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op = []
        
        for i in range(numRows):
            tmp = [1]
            for j in range(i):
                if j == i-1:
                    tmp.append(1)
                    break
                tmp.append(op[-1][j] + op[-1][j+1])
            op.append(tmp)
        
        return op