class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        res = []
        
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)
            
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
            
        return res