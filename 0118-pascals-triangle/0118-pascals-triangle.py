class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = []
        
        for i in range(n+1):
            tmp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j-1] + res[i-1][j])
            
            res.append(tmp)
        
        return res[1:]