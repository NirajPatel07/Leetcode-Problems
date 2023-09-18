class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        lookup = []
        
        for i, row in enumerate(mat):
            lookup.append([i, row.count(1)])
            
        lookup.sort(key=lambda x: x[1])
        
        res = []
        
        for i in range(k):
            res.append(lookup[i][0])
            
        return res